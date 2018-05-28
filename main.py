import sys
from antlr4 import *
from gen.DrapcodeLexer import DrapcodeLexer
from gen.DrapcodeParser import DrapcodeParser


def main(argv):
    input = FileStream(argv[1])
    lexer = DrapcodeLexer(input)
    stream = CommonTokenStream(lexer)
    parser = DrapcodeParser(stream)
    tree = parser.prog()

    print(tree)


if __name__ == '__main__':
    main(sys.argv)
