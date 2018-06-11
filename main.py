import sys
from antlr4 import *
from gen.DrapcodeLexer import DrapcodeLexer
from gen.DrapcodeParser import DrapcodeParser
from DrapcodeActions import DrapcodeActions


def main(argv):
    input_file = FileStream(argv[1])
    lexer = DrapcodeLexer(input_file)
    stream = CommonTokenStream(lexer)
    parser = DrapcodeParser(stream)
    tree = parser.prog()
    # print(tree)  # TODO for debug only

    walker = ParseTreeWalker()
    walker.walk(DrapcodeActions(), tree)


if __name__ == '__main__':
    main(sys.argv)
