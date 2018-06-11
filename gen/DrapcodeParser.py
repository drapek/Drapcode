# Generated from /home/drapek/HDD/Politechnika_Warszawska/SEM_8/JFIK/Project_3/project/src/Main/Drapcode.g4 by ANTLR 4.7
# encoding: utf-8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys

def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\r")
        buf.write("#\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\3\2\5\2\f\n\2\3\2\7")
        buf.write("\2\17\n\2\f\2\16\2\22\13\2\3\3\3\3\3\3\3\3\3\3\3\3\3\3")
        buf.write("\5\3\33\n\3\3\4\3\4\3\5\3\5\5\5!\n\5\3\5\2\2\6\2\4\6\b")
        buf.write("\2\3\4\2\3\3\n\n\2#\2\20\3\2\2\2\4\32\3\2\2\2\6\34\3\2")
        buf.write("\2\2\b \3\2\2\2\n\f\5\4\3\2\13\n\3\2\2\2\13\f\3\2\2\2")
        buf.write("\f\r\3\2\2\2\r\17\7\13\2\2\16\13\3\2\2\2\17\22\3\2\2\2")
        buf.write("\20\16\3\2\2\2\20\21\3\2\2\2\21\3\3\2\2\2\22\20\3\2\2")
        buf.write("\2\23\24\7\t\2\2\24\25\7\6\2\2\25\33\5\6\4\2\26\27\7\7")
        buf.write("\2\2\27\33\5\b\5\2\30\31\7\b\2\2\31\33\7\t\2\2\32\23\3")
        buf.write("\2\2\2\32\26\3\2\2\2\32\30\3\2\2\2\33\5\3\2\2\2\34\35")
        buf.write("\t\2\2\2\35\7\3\2\2\2\36!\7\t\2\2\37!\5\6\4\2 \36\3\2")
        buf.write("\2\2 \37\3\2\2\2!\t\3\2\2\2\6\13\20\32 ")
        return buf.getvalue()


class DrapcodeParser ( Parser ):

    grammarFileName = "Drapcode.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "'='", "'shout'", "'gimme'" ]

    symbolicNames = [ "<INVALID>", "NUMBER", "INTEGER", "FLOAT_NUMBER", 
                      "EQ", "PRINT", "READ", "ID", "STRING", "NEWLINE", 
                      "WS", "COMMENT" ]

    RULE_prog = 0
    RULE_stmt = 1
    RULE_var_def = 2
    RULE_var = 3

    ruleNames =  [ "prog", "stmt", "var_def", "var" ]

    EOF = Token.EOF
    NUMBER=1
    INTEGER=2
    FLOAT_NUMBER=3
    EQ=4
    PRINT=5
    READ=6
    ID=7
    STRING=8
    NEWLINE=9
    WS=10
    COMMENT=11

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
            self.state = 14
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << DrapcodeParser.PRINT) | (1 << DrapcodeParser.READ) | (1 << DrapcodeParser.ID) | (1 << DrapcodeParser.NEWLINE))) != 0):
                self.state = 9
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << DrapcodeParser.PRINT) | (1 << DrapcodeParser.READ) | (1 << DrapcodeParser.ID))) != 0):
                    self.state = 8
                    self.stmt()


                self.state = 11
                self.match(DrapcodeParser.NEWLINE)
                self.state = 16
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
        def var(self):
            return self.getTypedRuleContext(DrapcodeParser.VarContext,0)


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
            self.state = 24
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [DrapcodeParser.ID]:
                localctx = DrapcodeParser.AssignContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 17
                self.match(DrapcodeParser.ID)
                self.state = 18
                self.match(DrapcodeParser.EQ)
                self.state = 19
                self.var_def()
                pass
            elif token in [DrapcodeParser.PRINT]:
                localctx = DrapcodeParser.PrintContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 20
                self.match(DrapcodeParser.PRINT)
                self.state = 21
                self.var()
                pass
            elif token in [DrapcodeParser.READ]:
                localctx = DrapcodeParser.ReadContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 22
                self.match(DrapcodeParser.READ)
                self.state = 23
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

        def STRING(self):
            return self.getToken(DrapcodeParser.STRING, 0)

        def NUMBER(self):
            return self.getToken(DrapcodeParser.NUMBER, 0)

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
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 26
            _la = self._input.LA(1)
            if not(_la==DrapcodeParser.NUMBER or _la==DrapcodeParser.STRING):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class VarContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(DrapcodeParser.ID, 0)

        def var_def(self):
            return self.getTypedRuleContext(DrapcodeParser.Var_defContext,0)


        def getRuleIndex(self):
            return DrapcodeParser.RULE_var

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVar" ):
                listener.enterVar(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVar" ):
                listener.exitVar(self)




    def var(self):

        localctx = DrapcodeParser.VarContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_var)
        try:
            self.state = 30
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [DrapcodeParser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 28
                self.match(DrapcodeParser.ID)
                pass
            elif token in [DrapcodeParser.NUMBER, DrapcodeParser.STRING]:
                self.enterOuterAlt(localctx, 2)
                self.state = 29
                self.var_def()
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





