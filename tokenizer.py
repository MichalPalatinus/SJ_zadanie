# Author: Adam Kulisek, 3.12.2016
#
# Tokenizes input string (XML DTD)
# into predefined token classes
#
# Example input string : "<!ELEMENT last_name  (#PCDATA)>"

from token import Token
import re

class Tokenizer:
    # CLASS VARIABLES
    # token regular expressions
    WORD_REGEXP = "^([A-Za-z\_\:])[A-Za-z0-9\%\&\^\.\-\_\:]*$"
    REQUIRED_REGEXP = "^(#REQUIRED)$"
    IMPLIED_REGEXP = "^(#IMPLIED)$"
    FIXED_REGEXP = "^(#FIXED)$"
    CDATA_REGEXP = "^(CDATA)$"
    NMTOKEN_REGEXP = "^(NMTOKEN)$"
    IDREF_REGEXP = "^(IDREF)$"
    ATTLIST_REGEXP = "^(!ATTLIST)$"
    ELEMENT_REGEXP = "^(!ELEMENT)$"
    EMPTY_REGEXP = "^(EMPTY)$"
    ANY_REGEXP = "^(ANY)$"
    PCDATA_REGEXP = "^(\(#PCDATA\))$"

    SPECIAL_CHARS_DELIMITER_REGEXP = "([\,\|\"\(\)])"
    SPECIAL_CHARS_REGEXP = "^[\,\|\"\(\)\*\?\+]$"
    ANGLE_BRACKETS_REGEXP = "^[\<\>]$"

    # METHODS
    # does a string match a regexp?
    def regexpMatch(self, string, regexp):
        return bool(re.compile(regexp).search(string))

    # tokenize input sentences
    def tokenizeInput(self, input):
        tokens = []
        right_bracket_bool = False
        print "input: " + input
        if input[0] == '<':
            tokens.append(Token("SPECIAL", input[0]))
            input = input[1:]
        if input[-1] == '>':
            right_bracket_char = input[-1]
            input= input[:-1]
            right_bracket_bool = True
        if ' ' in input:
            words = input.split(' ')
        elif input == "(#PCDATA)":
            words = {input}
        else:
            words = re.split(self.SPECIAL_CHARS_DELIMITER_REGEXP, input)
        if len(words) == 1:
            print "Cannot split input anymore, type is NONE"
            tokens.append(Token("NONE", list(words)[0]))
            return tokens
        print "words: "
        for word in words:
            print "\t"+word
        for word in words:
            if word == '':
                continue
            if self.regexpMatch(word, self.REQUIRED_REGEXP):
                type = "REQUIRED"
            elif self.regexpMatch(word, self.IMPLIED_REGEXP):
                type = "IMPLIED"
            elif self.regexpMatch(word, self.FIXED_REGEXP):
                type = "FIXED"
            elif self.regexpMatch(word, self.CDATA_REGEXP):
                type = "CDATA"
            elif self.regexpMatch(word, self.NMTOKEN_REGEXP):
                type = "NMTOKEN"
            elif self.regexpMatch(word, self.IDREF_REGEXP):
                type = "IDREF"
            elif self.regexpMatch(word, self.ATTLIST_REGEXP):
                type = "ATTLIST"
            elif self.regexpMatch(word, self.ELEMENT_REGEXP):
                type = "ELEMENT"
            elif self.regexpMatch(word, self.EMPTY_REGEXP):
                type = "EMPTY"
            elif self.regexpMatch(word, self.ANY_REGEXP):
                type = "ANY"
            elif self.regexpMatch(word, self.PCDATA_REGEXP):
                type = "PCDATA"
            elif self.regexpMatch(word, self.WORD_REGEXP):
                type = "WORD"
            elif self.regexpMatch(word, self.SPECIAL_CHARS_REGEXP):
                type = "SPECIAL"
            else:
                type = "NONE"
            if type == "NONE":
                print("type is none")
                print(word)
                recursive_tokens = self.tokenizeInput(word)
                for recursive_token in recursive_tokens:
                    tokens.append(recursive_token)
            else:
                tokens.append(Token(type, word))

        if right_bracket_bool:
            tokens.append(Token("SPECIAL", right_bracket_char))
        print "tokens array length: " + str(len(tokens))
        print "tokens: "
        for token in tokens:
            print "\ttype: "+token.type+"\tvalue: "+token.value
        return tokens