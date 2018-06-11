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
        self.llvm_gen.print(self.value)

    # Exit a parse tree produced by DrapcodeParser#assign.
    def exitAssign(self, ctx: DrapcodeParser.AssignContext):
        self.global_variables[ctx.ID] = ctx.getText()[:-1]

    # Exit a parse tree produced by DrapcodeParser#var.
    def exitVar(self, ctx: DrapcodeParser.VarContext):
        if ctx.ID:
            self.value = self.global_variables[ctx.ID]
        else:
            if ctx.getText():
                self.value = ctx.getText()[:-1]
