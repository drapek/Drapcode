# Generated from /home/drapek/HDD/Politechnika_Warszawska/SEM_8/JFIK/Project_3/project/src/Main/Drapcode.g4 by ANTLR 4.7
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .DrapcodeParser import DrapcodeParser
else:
    from DrapcodeParser import DrapcodeParser

# This class defines a complete listener for a parse tree produced by DrapcodeParser.
class DrapcodeListener(ParseTreeListener):

    # Enter a parse tree produced by DrapcodeParser#prog.
    def enterProg(self, ctx:DrapcodeParser.ProgContext):
        pass

    # Exit a parse tree produced by DrapcodeParser#prog.
    def exitProg(self, ctx:DrapcodeParser.ProgContext):
        pass


    # Enter a parse tree produced by DrapcodeParser#while.
    def enterWhile(self, ctx:DrapcodeParser.WhileContext):
        pass

    # Exit a parse tree produced by DrapcodeParser#while.
    def exitWhile(self, ctx:DrapcodeParser.WhileContext):
        pass


    # Enter a parse tree produced by DrapcodeParser#if.
    def enterIf(self, ctx:DrapcodeParser.IfContext):
        pass

    # Exit a parse tree produced by DrapcodeParser#if.
    def exitIf(self, ctx:DrapcodeParser.IfContext):
        pass


    # Enter a parse tree produced by DrapcodeParser#assign.
    def enterAssign(self, ctx:DrapcodeParser.AssignContext):
        pass

    # Exit a parse tree produced by DrapcodeParser#assign.
    def exitAssign(self, ctx:DrapcodeParser.AssignContext):
        pass


    # Enter a parse tree produced by DrapcodeParser#print.
    def enterPrint(self, ctx:DrapcodeParser.PrintContext):
        pass

    # Exit a parse tree produced by DrapcodeParser#print.
    def exitPrint(self, ctx:DrapcodeParser.PrintContext):
        pass


    # Enter a parse tree produced by DrapcodeParser#read.
    def enterRead(self, ctx:DrapcodeParser.ReadContext):
        pass

    # Exit a parse tree produced by DrapcodeParser#read.
    def exitRead(self, ctx:DrapcodeParser.ReadContext):
        pass


    # Enter a parse tree produced by DrapcodeParser#funccall.
    def enterFunccall(self, ctx:DrapcodeParser.FunccallContext):
        pass

    # Exit a parse tree produced by DrapcodeParser#funccall.
    def exitFunccall(self, ctx:DrapcodeParser.FunccallContext):
        pass


    # Enter a parse tree produced by DrapcodeParser#while_cond.
    def enterWhile_cond(self, ctx:DrapcodeParser.While_condContext):
        pass

    # Exit a parse tree produced by DrapcodeParser#while_cond.
    def exitWhile_cond(self, ctx:DrapcodeParser.While_condContext):
        pass


    # Enter a parse tree produced by DrapcodeParser#if_cond.
    def enterIf_cond(self, ctx:DrapcodeParser.If_condContext):
        pass

    # Exit a parse tree produced by DrapcodeParser#if_cond.
    def exitIf_cond(self, ctx:DrapcodeParser.If_condContext):
        pass


    # Enter a parse tree produced by DrapcodeParser#blockwhile.
    def enterBlockwhile(self, ctx:DrapcodeParser.BlockwhileContext):
        pass

    # Exit a parse tree produced by DrapcodeParser#blockwhile.
    def exitBlockwhile(self, ctx:DrapcodeParser.BlockwhileContext):
        pass


    # Enter a parse tree produced by DrapcodeParser#blockif.
    def enterBlockif(self, ctx:DrapcodeParser.BlockifContext):
        pass

    # Exit a parse tree produced by DrapcodeParser#blockif.
    def exitBlockif(self, ctx:DrapcodeParser.BlockifContext):
        pass


    # Enter a parse tree produced by DrapcodeParser#blockfunc.
    def enterBlockfunc(self, ctx:DrapcodeParser.BlockfuncContext):
        pass

    # Exit a parse tree produced by DrapcodeParser#blockfunc.
    def exitBlockfunc(self, ctx:DrapcodeParser.BlockfuncContext):
        pass


    # Enter a parse tree produced by DrapcodeParser#block.
    def enterBlock(self, ctx:DrapcodeParser.BlockContext):
        pass

    # Exit a parse tree produced by DrapcodeParser#block.
    def exitBlock(self, ctx:DrapcodeParser.BlockContext):
        pass


    # Enter a parse tree produced by DrapcodeParser#var_def.
    def enterVar_def(self, ctx:DrapcodeParser.Var_defContext):
        pass

    # Exit a parse tree produced by DrapcodeParser#var_def.
    def exitVar_def(self, ctx:DrapcodeParser.Var_defContext):
        pass


    # Enter a parse tree produced by DrapcodeParser#single0.
    def enterSingle0(self, ctx:DrapcodeParser.Single0Context):
        pass

    # Exit a parse tree produced by DrapcodeParser#single0.
    def exitSingle0(self, ctx:DrapcodeParser.Single0Context):
        pass


    # Enter a parse tree produced by DrapcodeParser#add.
    def enterAdd(self, ctx:DrapcodeParser.AddContext):
        pass

    # Exit a parse tree produced by DrapcodeParser#add.
    def exitAdd(self, ctx:DrapcodeParser.AddContext):
        pass


    # Enter a parse tree produced by DrapcodeParser#single1.
    def enterSingle1(self, ctx:DrapcodeParser.Single1Context):
        pass

    # Exit a parse tree produced by DrapcodeParser#single1.
    def exitSingle1(self, ctx:DrapcodeParser.Single1Context):
        pass


    # Enter a parse tree produced by DrapcodeParser#sub.
    def enterSub(self, ctx:DrapcodeParser.SubContext):
        pass

    # Exit a parse tree produced by DrapcodeParser#sub.
    def exitSub(self, ctx:DrapcodeParser.SubContext):
        pass


    # Enter a parse tree produced by DrapcodeParser#single2.
    def enterSingle2(self, ctx:DrapcodeParser.Single2Context):
        pass

    # Exit a parse tree produced by DrapcodeParser#single2.
    def exitSingle2(self, ctx:DrapcodeParser.Single2Context):
        pass


    # Enter a parse tree produced by DrapcodeParser#mult.
    def enterMult(self, ctx:DrapcodeParser.MultContext):
        pass

    # Exit a parse tree produced by DrapcodeParser#mult.
    def exitMult(self, ctx:DrapcodeParser.MultContext):
        pass


    # Enter a parse tree produced by DrapcodeParser#single3.
    def enterSingle3(self, ctx:DrapcodeParser.Single3Context):
        pass

    # Exit a parse tree produced by DrapcodeParser#single3.
    def exitSingle3(self, ctx:DrapcodeParser.Single3Context):
        pass


    # Enter a parse tree produced by DrapcodeParser#div.
    def enterDiv(self, ctx:DrapcodeParser.DivContext):
        pass

    # Exit a parse tree produced by DrapcodeParser#div.
    def exitDiv(self, ctx:DrapcodeParser.DivContext):
        pass


    # Enter a parse tree produced by DrapcodeParser#int.
    def enterInt(self, ctx:DrapcodeParser.IntContext):
        pass

    # Exit a parse tree produced by DrapcodeParser#int.
    def exitInt(self, ctx:DrapcodeParser.IntContext):
        pass


    # Enter a parse tree produced by DrapcodeParser#float.
    def enterFloat(self, ctx:DrapcodeParser.FloatContext):
        pass

    # Exit a parse tree produced by DrapcodeParser#float.
    def exitFloat(self, ctx:DrapcodeParser.FloatContext):
        pass


    # Enter a parse tree produced by DrapcodeParser#expr_id.
    def enterExpr_id(self, ctx:DrapcodeParser.Expr_idContext):
        pass

    # Exit a parse tree produced by DrapcodeParser#expr_id.
    def exitExpr_id(self, ctx:DrapcodeParser.Expr_idContext):
        pass


    # Enter a parse tree produced by DrapcodeParser#par.
    def enterPar(self, ctx:DrapcodeParser.ParContext):
        pass

    # Exit a parse tree produced by DrapcodeParser#par.
    def exitPar(self, ctx:DrapcodeParser.ParContext):
        pass


    # Enter a parse tree produced by DrapcodeParser#var_num.
    def enterVar_num(self, ctx:DrapcodeParser.Var_numContext):
        pass

    # Exit a parse tree produced by DrapcodeParser#var_num.
    def exitVar_num(self, ctx:DrapcodeParser.Var_numContext):
        pass


    # Enter a parse tree produced by DrapcodeParser#cond_eq.
    def enterCond_eq(self, ctx:DrapcodeParser.Cond_eqContext):
        pass

    # Exit a parse tree produced by DrapcodeParser#cond_eq.
    def exitCond_eq(self, ctx:DrapcodeParser.Cond_eqContext):
        pass


    # Enter a parse tree produced by DrapcodeParser#cond_gt.
    def enterCond_gt(self, ctx:DrapcodeParser.Cond_gtContext):
        pass

    # Exit a parse tree produced by DrapcodeParser#cond_gt.
    def exitCond_gt(self, ctx:DrapcodeParser.Cond_gtContext):
        pass


    # Enter a parse tree produced by DrapcodeParser#cond_gte.
    def enterCond_gte(self, ctx:DrapcodeParser.Cond_gteContext):
        pass

    # Exit a parse tree produced by DrapcodeParser#cond_gte.
    def exitCond_gte(self, ctx:DrapcodeParser.Cond_gteContext):
        pass


    # Enter a parse tree produced by DrapcodeParser#cond_lt.
    def enterCond_lt(self, ctx:DrapcodeParser.Cond_ltContext):
        pass

    # Exit a parse tree produced by DrapcodeParser#cond_lt.
    def exitCond_lt(self, ctx:DrapcodeParser.Cond_ltContext):
        pass


    # Enter a parse tree produced by DrapcodeParser#cond_lte.
    def enterCond_lte(self, ctx:DrapcodeParser.Cond_lteContext):
        pass

    # Exit a parse tree produced by DrapcodeParser#cond_lte.
    def exitCond_lte(self, ctx:DrapcodeParser.Cond_lteContext):
        pass


    # Enter a parse tree produced by DrapcodeParser#cond_diff.
    def enterCond_diff(self, ctx:DrapcodeParser.Cond_diffContext):
        pass

    # Exit a parse tree produced by DrapcodeParser#cond_diff.
    def exitCond_diff(self, ctx:DrapcodeParser.Cond_diffContext):
        pass


    # Enter a parse tree produced by DrapcodeParser#function.
    def enterFunction(self, ctx:DrapcodeParser.FunctionContext):
        pass

    # Exit a parse tree produced by DrapcodeParser#function.
    def exitFunction(self, ctx:DrapcodeParser.FunctionContext):
        pass


    # Enter a parse tree produced by DrapcodeParser#f_head.
    def enterF_head(self, ctx:DrapcodeParser.F_headContext):
        pass

    # Exit a parse tree produced by DrapcodeParser#f_head.
    def exitF_head(self, ctx:DrapcodeParser.F_headContext):
        pass


