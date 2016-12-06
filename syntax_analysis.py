from token import Token
from tokenizer import Tokenizer
import re

class SyntaxAnalysis:
    # grammar rules in a form of string:
    #   - @ denotes epsilon
    #   - . denotes empty item = error
    GRAMMAR = \
    " < > ( ) | , \" ? * +\n\
A . . . . @ . . . . .\n\
B . . . . . . . . . .\n\
C . . . . . . . . . .\n\
D . . . . . . . . . .\n\
E . . . . . . . . . .\n\
F . . . . . . . . . .\n"
    # parse table structure:
    #     < > ( ) | , " ? * + WORD REQUIRED IMPLIED FIXED CDATA NMTOKEN IDREF ATTLIST ELEMENT EMPTY ANY PCDATA
    #   A
    #   B
    #   C
    #   D
    #   E
    #   F
    #   G
    #
    #   parse table is represented as a hash table of parse table row indexes
    #   (non terminals + terminals) where each of the hash values is another
    #   hash table with the column indexes as keys and set of terminas and
    #   nonterminals delimited by space for the given rule
    #
    PARSE_TABLE = {}
    def initializeParseTable(self):
        rows = filter(None,self.GRAMMAR.split('\n'))
        columns_indexes = filter(None,rows[0].split(' '))
        for row in rows[1:]:
            columns = row[2:].split(' ')
            self.PARSE_TABLE[row[0]] = {}
            for idx, column in enumerate(columns):
                print(idx, column)
                self.PARSE_TABLE[row[0]][columns_indexes[idx]] = column


    def analyzeTokens(self, tokens):
        stack = []
        stack.append('A')
        pop = stack.pop()
        print "\n\n\n\tPARSE TABLE: \n"
        for key in self.PARSE_TABLE:
            print self.PARSE_TABLE[key].iterkeys().next() + " | "
            for second_key in self.PARSE_TABLE[key]:
                    print self.PARSE_TABLE[key][second_key]
            print "\n"

        return True
