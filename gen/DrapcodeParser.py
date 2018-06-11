# Generated from /home/drapek/HDD/Politechnika_Warszawska/SEM_8/JFIK/Project_3/project/src/Main/Drapcode.g4 by ANTLR 4.7
# encoding: utf-8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys

def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\22")
        buf.write("L\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b")
        buf.write("\t\b\4\t\t\t\3\2\5\2\24\n\2\3\2\7\2\27\n\2\f\2\16\2\32")
        buf.write("\13\2\3\3\3\3\3\3\3\3\3\3\3\3\3\3\5\3#\n\3\3\4\3\4\3\5")
        buf.write("\3\5\3\5\3\5\3\5\5\5,\n\5\3\6\3\6\3\6\3\6\3\6\5\6\63\n")
        buf.write("\6\3\7\3\7\3\7\3\7\3\7\5\7:\n\7\3\b\3\b\3\b\3\b\3\b\5")
        buf.write("\bA\n\b\3\t\3\t\3\t\3\t\3\t\3\t\3\t\5\tJ\n\t\3\t\2\2\n")
        buf.write("\2\4\6\b\n\f\16\20\2\2\2N\2\30\3\2\2\2\4\"\3\2\2\2\6$")
        buf.write("\3\2\2\2\b+\3\2\2\2\n\62\3\2\2\2\f9\3\2\2\2\16@\3\2\2")
        buf.write("\2\20I\3\2\2\2\22\24\5\4\3\2\23\22\3\2\2\2\23\24\3\2\2")
        buf.write("\2\24\25\3\2\2\2\25\27\7\20\2\2\26\23\3\2\2\2\27\32\3")
        buf.write("\2\2\2\30\26\3\2\2\2\30\31\3\2\2\2\31\3\3\2\2\2\32\30")
        buf.write("\3\2\2\2\33\34\7\16\2\2\34\35\7\13\2\2\35#\5\6\4\2\36")
        buf.write("\37\7\f\2\2\37#\7\16\2\2 !\7\r\2\2!#\7\16\2\2\"\33\3\2")
        buf.write("\2\2\"\36\3\2\2\2\" \3\2\2\2#\5\3\2\2\2$%\5\b\5\2%\7\3")
        buf.write("\2\2\2&,\5\n\6\2\'(\5\n\6\2()\7\t\2\2)*\5\n\6\2*,\3\2")
        buf.write("\2\2+&\3\2\2\2+\'\3\2\2\2,\t\3\2\2\2-\63\5\f\7\2./\5\f")
        buf.write("\7\2/\60\7\n\2\2\60\61\5\f\7\2\61\63\3\2\2\2\62-\3\2\2")
        buf.write("\2\62.\3\2\2\2\63\13\3\2\2\2\64:\5\16\b\2\65\66\5\16\b")
        buf.write("\2\66\67\7\7\2\2\678\5\16\b\28:\3\2\2\29\64\3\2\2\29\65")
        buf.write("\3\2\2\2:\r\3\2\2\2;A\5\20\t\2<=\5\20\t\2=>\7\b\2\2>?")
        buf.write("\5\20\t\2?A\3\2\2\2@;\3\2\2\2@<\3\2\2\2A\17\3\2\2\2BJ")
        buf.write("\7\5\2\2CJ\7\6\2\2DJ\7\16\2\2EF\7\3\2\2FG\5\b\5\2GH\7")
        buf.write("\4\2\2HJ\3\2\2\2IB\3\2\2\2IC\3\2\2\2ID\3\2\2\2IE\3\2\2")
        buf.write("\2J\21\3\2\2\2\n\23\30\"+\629@I")
        return buf.getvalue()


class DrapcodeParser ( Parser ):

    grammarFileName = "Drapcode.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'('", "')'", "<INVALID>", "<INVALID>", 
                     "'*'", "'/'", "'+'", "'-'", "'='", "'shout'", "'gimme'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "INTEGER", 
                      "FLOAT_NUMBER", "MULT", "DIV", "ADD", "MINUS", "EQ", 
                      "PRINT", "READ", "ID", "STRING", "NEWLINE", "WS", 
                      "COMMENT" ]

    RULE_prog = 0
    RULE_stmt = 1
    RULE_var_def = 2
    RULE_expr0 = 3
    RULE_expr1 = 4
    RULE_expr2 = 5
    RULE_expr3 = 6
    RULE_expr4 = 7

    ruleNames =  [ "prog", "stmt", "var_def", "expr0", "expr1", "expr2", 
                   "expr3", "expr4" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    INTEGER=3
    FLOAT_NUMBER=4
    MULT=5
    DIV=6
    ADD=7
    MINUS=8
    EQ=9
    PRINT=10
    READ=11
    ID=12
    STRING=13
    NEWLINE=14
    WS=15
    COMMENT=16

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None



    class ProgContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NEWLINE(self, i:int=None):
            if i is None:
                return self.getTokens(DrapcodeParser.NEWLINE)
            else:
                return self.getToken(DrapcodeParser.NEWLINE, i)

        def stmt(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(DrapcodeParser.StmtContext)
            else:
                return self.getTypedRuleContext(DrapcodeParser.StmtContext,i)


        def getRuleIndex(self):
            return DrapcodeParser.RULE_prog

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProg" ):
                listener.enterProg(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProg" ):
                listener.exitProg(self)




    def prog(self):

        localctx = DrapcodeParser.ProgContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_prog)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 22
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << DrapcodeParser.PRINT) | (1 << DrapcodeParser.READ) | (1 << DrapcodeParser.ID) | (1 << DrapcodeParser.NEWLINE))) != 0):
                self.state = 17
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << DrapcodeParser.PRINT) | (1 << DrapcodeParser.READ) | (1 << DrapcodeParser.ID))) != 0):
                    self.state = 16
                    self.stmt()


                self.state = 19
                self.match(DrapcodeParser.NEWLINE)
                self.state = 24
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class StmtContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return DrapcodeParser.RULE_stmt

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class PrintContext(StmtContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a DrapcodeParser.StmtContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def PRINT(self):
            return self.getToken(DrapcodeParser.PRINT, 0)
        def ID(self):
            return self.getToken(DrapcodeParser.ID, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrint" ):
                listener.enterPrint(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrint" ):
                listener.exitPrint(self)


    class ReadContext(StmtContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a DrapcodeParser.StmtContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def READ(self):
            return self.getToken(DrapcodeParser.READ, 0)
        def ID(self):
            return self.getToken(DrapcodeParser.ID, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRead" ):
                listener.enterRead(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRead" ):
                listener.exitRead(self)


    class AssignContext(StmtContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a DrapcodeParser.StmtContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(DrapcodeParser.ID, 0)
        def EQ(self):
            return self.getToken(DrapcodeParser.EQ, 0)
        def var_def(self):
            return self.getTypedRuleContext(DrapcodeParser.Var_defContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssign" ):
                listener.enterAssign(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssign" ):
                listener.exitAssign(self)



    def stmt(self):

        localctx = DrapcodeParser.StmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_stmt)
        try:
            self.state = 32
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [DrapcodeParser.ID]:
                localctx = DrapcodeParser.AssignContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 25
                self.match(DrapcodeParser.ID)
                self.state = 26
                self.match(DrapcodeParser.EQ)
                self.state = 27
                self.var_def()
                pass
            elif token in [DrapcodeParser.PRINT]:
                localctx = DrapcodeParser.PrintContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 28
                self.match(DrapcodeParser.PRINT)
                self.state = 29
                self.match(DrapcodeParser.ID)
                pass
            elif token in [DrapcodeParser.READ]:
                localctx = DrapcodeParser.ReadContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 30
                self.match(DrapcodeParser.READ)
                self.state = 31
                self.match(DrapcodeParser.ID)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Var_defContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr0(self):
            return self.getTypedRuleContext(DrapcodeParser.Expr0Context,0)


        def getRuleIndex(self):
            return DrapcodeParser.RULE_var_def

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVar_def" ):
                listener.enterVar_def(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVar_def" ):
                listener.exitVar_def(self)




    def var_def(self):

        localctx = DrapcodeParser.Var_defContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_var_def)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 34
            self.expr0()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Expr0Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return DrapcodeParser.RULE_expr0

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class Single0Context(Expr0Context):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a DrapcodeParser.Expr0Context
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr1(self):
            return self.getTypedRuleContext(DrapcodeParser.Expr1Context,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSingle0" ):
                listener.enterSingle0(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSingle0" ):
                listener.exitSingle0(self)


    class AddContext(Expr0Context):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a DrapcodeParser.Expr0Context
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr1(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(DrapcodeParser.Expr1Context)
            else:
                return self.getTypedRuleContext(DrapcodeParser.Expr1Context,i)

        def ADD(self):
            return self.getToken(DrapcodeParser.ADD, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAdd" ):
                listener.enterAdd(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAdd" ):
                listener.exitAdd(self)



    def expr0(self):

        localctx = DrapcodeParser.Expr0Context(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_expr0)
        try:
            self.state = 41
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                localctx = DrapcodeParser.Single0Context(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 36
                self.expr1()
                pass

            elif la_ == 2:
                localctx = DrapcodeParser.AddContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 37
                self.expr1()
                self.state = 38
                self.match(DrapcodeParser.ADD)
                self.state = 39
                self.expr1()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Expr1Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return DrapcodeParser.RULE_expr1

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class Single1Context(Expr1Context):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a DrapcodeParser.Expr1Context
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr2(self):
            return self.getTypedRuleContext(DrapcodeParser.Expr2Context,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSingle1" ):
                listener.enterSingle1(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSingle1" ):
                listener.exitSingle1(self)


    class SubContext(Expr1Context):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a DrapcodeParser.Expr1Context
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr2(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(DrapcodeParser.Expr2Context)
            else:
                return self.getTypedRuleContext(DrapcodeParser.Expr2Context,i)

        def MINUS(self):
            return self.getToken(DrapcodeParser.MINUS, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSub" ):
                listener.enterSub(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSub" ):
                listener.exitSub(self)



    def expr1(self):

        localctx = DrapcodeParser.Expr1Context(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_expr1)
        try:
            self.state = 48
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                localctx = DrapcodeParser.Single1Context(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 43
                self.expr2()
                pass

            elif la_ == 2:
                localctx = DrapcodeParser.SubContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 44
                self.expr2()
                self.state = 45
                self.match(DrapcodeParser.MINUS)
                self.state = 46
                self.expr2()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Expr2Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return DrapcodeParser.RULE_expr2

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class Single2Context(Expr2Context):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a DrapcodeParser.Expr2Context
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr3(self):
            return self.getTypedRuleContext(DrapcodeParser.Expr3Context,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSingle2" ):
                listener.enterSingle2(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSingle2" ):
                listener.exitSingle2(self)


    class MultContext(Expr2Context):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a DrapcodeParser.Expr2Context
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr3(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(DrapcodeParser.Expr3Context)
            else:
                return self.getTypedRuleContext(DrapcodeParser.Expr3Context,i)

        def MULT(self):
            return self.getToken(DrapcodeParser.MULT, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMult" ):
                listener.enterMult(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMult" ):
                listener.exitMult(self)



    def expr2(self):

        localctx = DrapcodeParser.Expr2Context(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_expr2)
        try:
            self.state = 55
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                localctx = DrapcodeParser.Single2Context(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 50
                self.expr3()
                pass

            elif la_ == 2:
                localctx = DrapcodeParser.MultContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 51
                self.expr3()
                self.state = 52
                self.match(DrapcodeParser.MULT)
                self.state = 53
                self.expr3()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Expr3Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return DrapcodeParser.RULE_expr3

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class DivContext(Expr3Context):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a DrapcodeParser.Expr3Context
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr4(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(DrapcodeParser.Expr4Context)
            else:
                return self.getTypedRuleContext(DrapcodeParser.Expr4Context,i)

        def DIV(self):
            return self.getToken(DrapcodeParser.DIV, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDiv" ):
                listener.enterDiv(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDiv" ):
                listener.exitDiv(self)


    class Single3Context(Expr3Context):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a DrapcodeParser.Expr3Context
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr4(self):
            return self.getTypedRuleContext(DrapcodeParser.Expr4Context,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSingle3" ):
                listener.enterSingle3(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSingle3" ):
                listener.exitSingle3(self)



    def expr3(self):

        localctx = DrapcodeParser.Expr3Context(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_expr3)
        try:
            self.state = 62
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                localctx = DrapcodeParser.Single3Context(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 57
                self.expr4()
                pass

            elif la_ == 2:
                localctx = DrapcodeParser.DivContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 58
                self.expr4()
                self.state = 59
                self.match(DrapcodeParser.DIV)
                self.state = 60
                self.expr4()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Expr4Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return DrapcodeParser.RULE_expr4

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class ParContext(Expr4Context):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a DrapcodeParser.Expr4Context
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr0(self):
            return self.getTypedRuleContext(DrapcodeParser.Expr0Context,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPar" ):
                listener.enterPar(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPar" ):
                listener.exitPar(self)


    class FloatContext(Expr4Context):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a DrapcodeParser.Expr4Context
            super().__init__(parser)
            self.copyFrom(ctx)

        def FLOAT_NUMBER(self):
            return self.getToken(DrapcodeParser.FLOAT_NUMBER, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFloat" ):
                listener.enterFloat(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFloat" ):
                listener.exitFloat(self)


    class IntContext(Expr4Context):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a DrapcodeParser.Expr4Context
            super().__init__(parser)
            self.copyFrom(ctx)

        def INTEGER(self):
            return self.getToken(DrapcodeParser.INTEGER, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInt" ):
                listener.enterInt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInt" ):
                listener.exitInt(self)


    class Expr_idContext(Expr4Context):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a DrapcodeParser.Expr4Context
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(DrapcodeParser.ID, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpr_id" ):
                listener.enterExpr_id(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpr_id" ):
                listener.exitExpr_id(self)



    def expr4(self):

        localctx = DrapcodeParser.Expr4Context(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_expr4)
        try:
            self.state = 71
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [DrapcodeParser.INTEGER]:
                localctx = DrapcodeParser.IntContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 64
                self.match(DrapcodeParser.INTEGER)
                pass
            elif token in [DrapcodeParser.FLOAT_NUMBER]:
                localctx = DrapcodeParser.FloatContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 65
                self.match(DrapcodeParser.FLOAT_NUMBER)
                pass
            elif token in [DrapcodeParser.ID]:
                localctx = DrapcodeParser.Expr_idContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 66
                self.match(DrapcodeParser.ID)
                pass
            elif token in [DrapcodeParser.T__0]:
                localctx = DrapcodeParser.ParContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 67
                self.match(DrapcodeParser.T__0)
                self.state = 68
                self.expr0()
                self.state = 69
                self.match(DrapcodeParser.T__1)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





