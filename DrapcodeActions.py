from LLVMGenerator import LLVMGenerator

from gen.DrapcodeListener import DrapcodeListener
from gen.DrapcodeParser import DrapcodeParser


class DrapcodeActions(DrapcodeListener):
    calc_stack = []
    declared_vars = []
    llvm_gen = LLVMGenerator()
    global_variables = {}  # temporary leaved unused, it will be needed for when global prefix will be available
    variables = []  # this is array of variables for each scope
    actual_scope = 0
    value = ""  # value of last proceed variable. Needed for printing it out.

    def __init__(self):
        self.variables.append({})

    def exitProg(self, ctx: DrapcodeParser.ProgContext):
        print(self.llvm_gen.generate())

    def exitPrint(self, ctx: DrapcodeParser.PrintContext):
        if hasattr(ctx, 'ID'):
            var_name = ctx.ID().getText()
            found_var = self.__search_in_scopes(var_name)
            self.llvm_gen.print(var_name, found_var.get_type())

    def exitAssign(self, ctx: DrapcodeParser.AssignContext):
        stack_variable = self.calc_stack.pop()
        var = self.__get_or_declare_variable_if_not_exists(ctx.ID().getText(), variable_type=stack_variable.get_type())
        var.value = stack_variable.get_value()
        self.llvm_gen.assign(ctx.ID().getText(), var.get_value(), var.get_type())

    def exitRead(self, ctx: DrapcodeParser.ReadContext):
        var = self.__get_or_declare_variable_if_not_exists(ctx.ID().getText())
        self.llvm_gen.scanf(ctx.ID().getText(), var.get_type())
        var.value = f"%{ctx.ID().getText()}"  # Save the register addr instead last value

    def exitInt(self, ctx:DrapcodeParser.IntContext):
        self.calc_stack.append(Variable(ctx.INTEGER().getText(), var_type="int"))

    def exitFloat(self, ctx:DrapcodeParser.FloatContext):
        self.calc_stack.append(Variable(ctx.FLOAT_NUMBER().getText(), var_type="double"))

    def exitExpr_id(self, ctx:DrapcodeParser.Expr_idContext):
        var = self.__search_in_scopes(ctx.ID().getText())
        self.calc_stack.append(var)

    def exitAdd(self, ctx:DrapcodeParser.AddContext):
        self.__apply_arithmetic_operation(self.llvm_gen.add_int, self.llvm_gen.add_double)

    def exitSub(self, ctx: DrapcodeParser.SubContext):
        self.__apply_arithmetic_operation(self.llvm_gen.sub_int, self.llvm_gen.sub_double)

    def exitMult(self, ctx:DrapcodeParser.MultContext):
        self.__apply_arithmetic_operation(self.llvm_gen.mult_int, self.llvm_gen.mult_double)

    def exitDiv(self, ctx:DrapcodeParser.DivContext):
        self.__apply_arithmetic_operation(self.llvm_gen.div_int, self.llvm_gen.div_double)

    def exitIf(self, ctx:DrapcodeParser.IfContext):
        pass

    def enterBlockif(self, ctx:DrapcodeParser.BlockContext):
        self.llvm_gen.if_start()
        self.__open_scope()

    def exitBlockif(self, ctx:DrapcodeParser.BlockContext):
        self.llvm_gen.if_end()
        self.__close_scope()

    def enterBlockwhile(self, ctx:DrapcodeParser.BlockwhileContext):
        self.llvm_gen.while_start()
        self.__open_scope()

    def exitBlockwhile(self, ctx:DrapcodeParser.BlockwhileContext):
        self.llvm_gen.while_end()
        self.__close_scope()

    def exitCond_eq(self, ctx:DrapcodeParser.Cond_eqContext):
        var_1 = ctx.var_num()[0]
        var_2 = ctx.var_num()[1]

        val_1 = self.__get_var_num_value(var_1)
        val_2 = self.__get_var_num_value(var_2)

        self.llvm_gen.icmp(val_1, val_2)

    def __search_in_scopes(self, var_name):
        """
        This function will return found Variable class of the name <var_name> with the nearest scope.
        :param var_name:
        :return:
        """
        for i in range(self.actual_scope, -1, -1):
            try:
                return self.variables[i][var_name]
            except KeyError:
                pass

        return None

    def __open_scope(self):
        self.actual_scope += 1
        try:
            self.variables[self.actual_scope] = {}
        except IndexError:
            self.variables.append({})

    def __close_scope(self):
        # when scope is closed we need to restore previous variable values in llvm
        # TODO compare with all scopes from actual to 0. Not only with 0.
        vars_that_changed = self.variables[0].keys() & self.variables[self.actual_scope].keys()
        for var_name in vars_that_changed:
            old_var = self.variables[0][var_name]
            # Restore the old value for this variables
            self.llvm_gen.assign(var_name, old_var.get_value(), old_var.get_type())
        # than we need to clear this scope
        self.actual_scope -= 1

    def __get_var_num_value(self, origin_ctx):
        if origin_ctx.ID() is not None:
            var_name = origin_ctx.ID().getText()
            return self.variables[self.actual_scope][var_name].get_value()
        else:
            return origin_ctx.INTEGER().getText()

    def __get_or_declare_variable_if_not_exists(self, variable_name, variable_value=None, variable_type=None):
        if variable_name not in self.variables[self.actual_scope].keys():
            var = Variable(variable_value, variable_type)
            # If it was declared in llvm than only assign new value
            if variable_name not in self.declared_vars:
                self.llvm_gen.declare(variable_name, var.type)
                self.declared_vars.append(variable_name)
            else:
                self.llvm_gen.assign(variable_name, var.get_value(), var.get_type())
            self.variables[self.actual_scope][variable_name] = var  # save it into global variables stack

        return self.variables[self.actual_scope][variable_name]

    def __apply_arithmetic_operation(self, llvm_dest_func_int, llvm_dest_func_double):
        value_1 = self.calc_stack.pop()
        value_2 = self.calc_stack.pop()

        if value_1.get_type() != value_2.get_type():
            # when int and double meets, convert the int to double
            if value_1.get_type() == "int":
                self.__convert_to_double(value_1)

            if value_2.get_type() == "int":
                self.__convert_to_double(value_2)

        if value_1.get_type() == "int":
            llvm_dest_func_int(value_2.get_value(), value_1.get_value())

        if value_1.get_type() == "double":
            llvm_dest_func_double(value_2.get_value(), value_1.get_value())

        # insert the result (address of the register where result is stored)
        self.calc_stack.append(Variable(f"%{self.llvm_gen.reg_iter-1}", var_type=value_1.get_type()))

    def __convert_to_double(self, variable):
        variable.value = f"{variable.get_value()}.0"
        variable.type = "double"
        return variable


class Variable:
    def __init__(self, value=None, var_type=None):
        if value is not None:
            self.value = value
        else:
            # If we don't have value, we can't predict it. So assign Double to it as default.
            self.value = 0
            if var_type is None:
                self.type = "double"
            else:
                self.type = var_type
            return

        if var_type is None:
            self.type = self.__recognize_var_type(value)
        else:
            self.type = var_type  # Auto assign double value

    def get_value(self):
        return str(self.value)

    def get_type(self):
        return self.type

    def __recognize_var_type(self, value):
        """
        This function can recognize only int or double
        :param value:
        :return:
        """
        if type(eval(value)) == int:
            return "int"
        if type(eval(value)) == float:
            return "double"  # because llvm has float and double, and the double is greater
        raise ValueError("Inappropriate type to declare.")
