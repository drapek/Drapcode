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
            self.llvm_gen.print(ctx.var().ID())

    # Exit a parse tree produced by DrapcodeParser#assign.
    def exitAssign(self, ctx: DrapcodeParser.AssignContext):
        # TODO recognize and save proper type into global_variables
        value = ctx.var_def().getText()
        self.__declare_variable_if_not_exists(ctx.ID())
        self.llvm_gen.assign(ctx.ID(), value)  # TODO this is probably sufficient only for INT
        self.global_variables[ctx.ID()] = value

    # Exit a parse tree produced by DrapcodeParser#read.
    def exitRead(self, ctx: DrapcodeParser.ReadContext):
        self.__declare_variable_if_not_exists(ctx.ID())
        self.llvm_gen.scanf(ctx.ID())

    # Exit a parse tree produced by DrapcodeParser#var.
    # def exitVar(self, ctx: DrapcodeParser.VarContext):
    #     if ctx.ID:
    #         self.value = self.global_variables[ctx.ID]
    #     else:
    #         if ctx.getText():
    #             self.value = ctx.getText()[:-1]

    def __declare_variable_if_not_exists(self, variable_name):
        if variable_name not in self.global_variables:
            self.llvm_gen.declare(variable_name)
