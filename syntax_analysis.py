from token import Token
from tokenizer import Tokenizer
import re

class SyntaxAnalysis:
    # grammar rules in a form of string:
    #   - @ denotes epsilon
    #   - . denotes empty item = error
    GRAMMAR = \
    " REQUIRED IMPLIED FIXED CDATA NMTOKEN IDREF ATTLIST ELEMENT EMPTY ANY PCDATA WORD , | \" ( ) < > ? * + $\n\
DTDOC . . . . . . . . . . . . . . . . . L;DECLARATION;< . . . . .\n\
L . . . . . . . . . . . . . . . . . DTDOC . . . . @\n\
DECLARATION . . . . . . >;Z;WORD;ATTLIST >;X;WORD;ELEMENT . . . . . . . . . . . . . . .\n\
X . . . . . . . . EMPTY ANY PCDATA . . . . );F;( . . . . . . .\n\
F . . . . . . . . . . . . . . . Y;K;CP;( . . . . . . .\n\
Y . . . . . . . . . . . . @ @ . . @ . . ? * + .\n\
H . . . . . . . . . . . . H;CP;, . . . @ . . . . . .\n\
K . . . . . . . . . . . . );H;CP;, );CP;| . . ) . . . . . .\n\
CP . . . . . . . . . . . Y;WORD . . . Y;K;CP;( . . . . . . .\n\
Z . . . . . . . . . . . Z;DEFAULTDECL;ATTRTYPE;WORD . . . . . . @ . . . .\n\
ATTRTYPE . . . CDATA NMTOKEN IDREF . . . . . . . . . );E;WORD;( . . . . . . .\n\
E . . . . . . . . . . . . . WORD;| . . @ . . . . . .\n\
DEFAULTDECL REQUIRED IMPLIED \";B;WORD;\";J . . . . . . . . . . . \";B;WORD;\";J . . . . . . . .\n\
J . . FIXED . . . . . . . . . . . @ . . . . . . . .\n\
B . . . . . . . . . . . B;WORD . . @ . . . . . . . .\n"

    # parse table structure:
    #      REQUIRED IMPLIED FIXED CDATA NMTOKEN IDREF ATTLIST ELEMENT EMPTY ANY PCDATA WORD , | \" ( ) < > ? * + $
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
            columns = row[0:].split(' ')
            self.PARSE_TABLE[columns[0]] = {}
            for idx, column in enumerate(columns[1:]):
                print(columns[0], columns_indexes[idx], column)
                self.PARSE_TABLE[columns[0]][columns_indexes[idx]] = column


    def analyzeTokens(self, tokens):
        stack = []
        stack.append('$')
        stack.append('DTDOC')
        position = 0
        pop = stack[len(stack)-1]
        while pop is not "$":
            print("Stack: " + str(stack))
            print("Top of Stack: " + pop)
            print("Token: " + token)
            pop = stack[len(stack) - 1]
            if tokens[position].type in {'SPECIAL', 'EOF'}:
                token = tokens[position].value
            else:
                token = tokens[position].type
            #print(token, pop)
            if pop not in self.PARSE_TABLE.keys() or pop is "$":
                if token == pop:
                    stack.pop()
                    position += 1
                    print("Top Of Stack equals Token, so we pop Top of Stack and move to another token.")
                elif pop == "@":
                    stack.pop()
                else:
                    print("******** Error 1*************")
                    position, stack = self.recovery(tokens, position, stack)
            else:
                if self.PARSE_TABLE[pop][token] != ".":
                    rules = self.PARSE_TABLE[pop][token].split(';')
                    stack.pop()
                    for rule in rules:
                        stack.append(rule)
                else:
                    print("************ Error 2 ****************")
                    position, stack = self.recovery(tokens, position, stack)

        print("Sentence accepted.")

    def recovery(self, tokens, position, stack):
        while tokens[position].value != ">":
            position += 1
        position += 1

        while stack[len(stack)-2] != '>':
            stack.pop()
        stack.pop()
        stack.pop()

        return position, stack




















