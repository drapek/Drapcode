# Generated from /home/drapek/HDD/Politechnika_Warszawska/SEM_8/JFIK/Project_3/project/src/Main/Drapcode.g4 by ANTLR 4.7
# encoding: utf-8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys

def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\23")
        buf.write("\33\4\2\t\2\4\3\t\3\4\4\t\4\3\2\5\2\n\n\2\3\2\7\2\r\n")
        buf.write("\2\f\2\16\2\20\13\2\3\3\3\3\3\3\3\3\3\3\5\3\27\n\3\3\4")
        buf.write("\3\4\3\4\2\2\5\2\4\6\2\3\3\2\6\7\2\32\2\16\3\2\2\2\4\26")
        buf.write("\3\2\2\2\6\30\3\2\2\2\b\n\5\4\3\2\t\b\3\2\2\2\t\n\3\2")
        buf.write("\2\2\n\13\3\2\2\2\13\r\7\r\2\2\f\t\3\2\2\2\r\20\3\2\2")
        buf.write("\2\16\f\3\2\2\2\16\17\3\2\2\2\17\3\3\2\2\2\20\16\3\2\2")
        buf.write("\2\21\22\7\4\2\2\22\27\5\6\4\2\23\24\7\6\2\2\24\25\7\3")
        buf.write("\2\2\25\27\7\7\2\2\26\21\3\2\2\2\26\23\3\2\2\2\27\5\3")
        buf.write("\2\2\2\30\31\t\2\2\2\31\7\3\2\2\2\5\t\16\26")
        return buf.getvalue()


class DrapcodeParser ( Parser ):

    grammarFileName = "Drapcode.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'='", "'shout'", "'gimme'", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "'['", "']'", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "'*'", "'+'", "'-'", "'/'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "PRINT", "READ", "ID", "STRING", 
                      "NUMBER", "INTEGER", "FLOAT_NUMBER", "OPEN_BRACK", 
                      "CLOSE_BRACK", "NEWLINE", "WS", "COMMENT", "STAR", 
                      "ADD", "MINUS", "DIV" ]

    RULE_prog = 0
    RULE_stat = 1
    RULE_value = 2

    ruleNames =  [ "prog", "stat", "value" ]

    EOF = Token.EOF
    T__0=1
    PRINT=2
    READ=3
    ID=4
    STRING=5
    NUMBER=6
    INTEGER=7
    FLOAT_NUMBER=8
    OPEN_BRACK=9
    CLOSE_BRACK=10
    NEWLINE=11
    WS=12
    COMMENT=13
    STAR=14
    ADD=15
    MINUS=16
    DIV=17

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

        def stat(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(DrapcodeParser.StatContext)
            else:
                return self.getTypedRuleContext(DrapcodeParser.StatContext,i)


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
            self.state = 12
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << DrapcodeParser.PRINT) | (1 << DrapcodeParser.ID) | (1 << DrapcodeParser.NEWLINE))) != 0):
                self.state = 7
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==DrapcodeParser.PRINT or _la==DrapcodeParser.ID:
                    self.state = 6
                    self.stat()


                self.state = 9
                self.match(DrapcodeParser.NEWLINE)
                self.state = 14
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class StatContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return DrapcodeParser.RULE_stat

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class PrintContext(StatContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a DrapcodeParser.StatContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def PRINT(self):
            return self.getToken(DrapcodeParser.PRINT, 0)
        def value(self):
            return self.getTypedRuleContext(DrapcodeParser.ValueContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrint" ):
                listener.enterPrint(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrint" ):
                listener.exitPrint(self)


    class AssignContext(StatContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a DrapcodeParser.StatContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(DrapcodeParser.ID, 0)
        def STRING(self):
            return self.getToken(DrapcodeParser.STRING, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssign" ):
                listener.enterAssign(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssign" ):
                listener.exitAssign(self)



    def stat(self):

        localctx = DrapcodeParser.StatContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_stat)
        try:
            self.state = 20
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [DrapcodeParser.PRINT]:
                localctx = DrapcodeParser.PrintContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 15
                self.match(DrapcodeParser.PRINT)
                self.state = 16
                self.value()
                pass
            elif token in [DrapcodeParser.ID]:
                localctx = DrapcodeParser.AssignContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 17
                self.match(DrapcodeParser.ID)
                self.state = 18
                self.match(DrapcodeParser.T__0)
                self.state = 19
                self.match(DrapcodeParser.STRING)
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

    class ValueContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(DrapcodeParser.ID, 0)

        def STRING(self):
            return self.getToken(DrapcodeParser.STRING, 0)

        def getRuleIndex(self):
            return DrapcodeParser.RULE_value

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterValue" ):
                listener.enterValue(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitValue" ):
                listener.exitValue(self)




    def value(self):

        localctx = DrapcodeParser.ValueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_value)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 22
            _la = self._input.LA(1)
            if not(_la==DrapcodeParser.ID or _la==DrapcodeParser.STRING):
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





