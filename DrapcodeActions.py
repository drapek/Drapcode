from LLVMGenerator import LLVMGenerator

from gen.DrapcodeListener import DrapcodeListener
from gen.DrapcodeParser import DrapcodeParser


class DrapcodeActions(DrapcodeListener):
    calc_stack = []
    llvm_gen = LLVMGenerator()
    global_variables = {}
    value = ""  # value of last proceed variable. Needed for printing it out.

    def exitProg(self, ctx: DrapcodeParser.ProgContext):
        print(self.llvm_gen.generate())

    def exitPrint(self, ctx: DrapcodeParser.PrintContext):
        if hasattr(ctx, 'ID'):
            var_name = ctx.ID().getText()
            found_var = self.global_variables[var_name]
            self.llvm_gen.print(var_name, found_var.get_type())

    def exitAssign(self, ctx: DrapcodeParser.AssignContext):
        stack_variable = self.calc_stack.pop()
        var = self.__get_or_declare_variable_if_not_exists(ctx.ID().getText(), variable_type=stack_variable.get_type())
        var.value = stack_variable.get_value()
        self.llvm_gen.assign(ctx.ID().getText(), var.get_value(), var.get_type())

    def exitRead(self, ctx: DrapcodeParser.ReadContext):
        var = self.__get_or_declare_variable_if_not_exists(ctx.ID().getText())
        self.llvm_gen.scanf(ctx.ID().getText(), var.get_type())

    def exitInt(self, ctx:DrapcodeParser.IntContext):
        self.calc_stack.append(Variable(ctx.INTEGER().getText(), var_type="int"))

    def exitFloat(self, ctx:DrapcodeParser.FloatContext):
        self.calc_stack.append(Variable(ctx.FLOAT_NUMBER().getText(), var_type="double"))

    def exitAdd(self, ctx:DrapcodeParser.AddContext):
        self.__apply_arithmetic_operation(self.llvm_gen.add_int, self.llvm_gen.add_double)

    def exitSub(self, ctx: DrapcodeParser.SubContext):
        self.__apply_arithmetic_operation(self.llvm_gen.sub_int, self.llvm_gen.sub_double)

    def exitMult(self, ctx:DrapcodeParser.MultContext):
        self.__apply_arithmetic_operation(self.llvm_gen.mult_int, self.llvm_gen.mult_double)

    def exitDiv(self, ctx:DrapcodeParser.DivContext):
        self.__apply_arithmetic_operation(self.llvm_gen.div_int, self.llvm_gen.div_double)

    def __get_or_declare_variable_if_not_exists(self, variable_name, variable_value=None, variable_type=None):
        if variable_name not in self.global_variables.keys():
            var = Variable(variable_value, variable_type)
            self.llvm_gen.declare(variable_name, var.type)
            self.global_variables[variable_name] = var  # save it into global variables stack

        return self.global_variables[variable_name]

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
