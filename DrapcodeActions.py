from LLVMGenerator import LLVMGenerator

from gen.DrapcodeListener import DrapcodeListener
from gen.DrapcodeParser import DrapcodeParser


class DrapcodeActions(DrapcodeListener):
    llvm_gen = LLVMGenerator()
    global_variables = {}
    value = ""  # value of last proceed variable. Needed for printing it out.

    # Exit a parse tree produced by DrapcodeParser#prog.
    def exitProg(self, ctx: DrapcodeParser.ProgContext):
        print(self.llvm_gen.generate())

    # Exit a parse tree produced by DrapcodeParser#print.
    def exitPrint(self, ctx: DrapcodeParser.PrintContext):
        if hasattr(ctx, 'var'):
            var_name = ctx.var().ID().getText()
            found_var = self.global_variables[var_name]
            self.llvm_gen.print(var_name, found_var.get_type())

    # Exit a parse tree produced by DrapcodeParser#assign.
    def exitAssign(self, ctx: DrapcodeParser.AssignContext):
        value = ctx.var_def().getText()
        var = self.__get_or_declare_variable_if_not_exists(ctx.ID().getText(), value)
        self.llvm_gen.assign(ctx.ID().getText(), var.get_value(), var.get_type())

    # Exit a parse tree produced by DrapcodeParser#read.
    def exitRead(self, ctx: DrapcodeParser.ReadContext):
        var = self.__get_or_declare_variable_if_not_exists(ctx.ID().getText())
        self.llvm_gen.scanf(ctx.ID().getText(), var.get_type())

    # Exit a parse tree produced by DrapcodeParser#var.
    # def exitVar(self, ctx: DrapcodeParser.VarContext):
    #     if ctx.ID:
    #         self.value = self.global_variables[ctx.ID]
    #     else:
    #         if ctx.getText():
    #             self.value = ctx.getText()[:-1]

    def __get_or_declare_variable_if_not_exists(self, variable_name, variable_value=None):
        if variable_name not in self.global_variables.keys():
            var = Variable(variable_value)
            self.llvm_gen.declare(variable_name, var.type)
            self.global_variables[variable_name] = var  # save it into global variables stack

        return self.global_variables[variable_name]


class Variable:
    def __init__(self, value=None, var_type=None):
        if value is not None:
            self.value = value
        else:
            # If we don't have value, we can't predict it. So assign Double to it as default.
            self.value = 0
            self.type = "double"
            return

        if var_type is None:
            self.type = self.__recognize_var_type(value)
        else:
            self.type = "double"  # Auto assign double value

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
