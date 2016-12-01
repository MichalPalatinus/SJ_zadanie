from token import Token
import re

class Tokenizer:
    # CLASS VARIABLES
    # lowest level regular expressions
    DIGIT = "[0-9]"
    LETTER = "[A-Za-z]"
    SPECIAL_CHAR = "[\#\^\&]"
    DIGIT_REGEXP = "^"+DIGIT+"$"
    LETTER_REGEXP = "^"+LETTER+"$"
    CHAR_REGEXP = "^("+DIGIT+"|"+LETTER+"|"+SPECIAL_CHAR+")$"
    NAMECHAR_REGEXP = "^("+DIGIT+"|"+LETTER+"|"+"[\.\-\:\_])$"
    # token regular expressions
    WORD_REGEXP = "^[0-9A-Za-z\&\^\#]+$"
    NAME_REGEXP = "^[A-Za-z\_\:][0-9A-Za-z\.\-\:\_]*$"
    REQUIRED_REGEXP = "#REQUIRED"
    IMPLIED_REGEXP = "#IMPLIED"
    FIXED_REGEXP = "#FIXED"
    CDATA_REGEXP = "^(CDATA)$"
    NMTOKEN_REGEXP = "NMTOKEN"
    IDREF_REGEXP = "IDREF"
    ATTLIST_REGEXP = "<!ATTLIST"
    ELEMENT_REGEXP = "<!ELEMENT"
    EMPTY_REGEXP = "EMPTY"
    ANY_REGEXP = "ANY"
    PCDATA_REGEXP = "(#PCDATA)"
    # METHODS
    # does a string match a regexp?
    def regexpMatch(self, string, regexp):
        return bool(re.compile(regexp).search(string))

    def tokenizeInput(self, input):
        tokens = []
        words = input.split(' ')
        for word in words:
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
            elif self.regexpMatch(word, self.NAME_REGEXP):
                type = "NAME"
            elif self.regexpMatch(word, self.WORD_REGEXP):
                type = "WORD"
            else:
                type = "NONE"

            tokens.append(Token(type, word))

        print "tokens array length: " + str(len(tokens))
        print "tokens: "
        for token in tokens:
            print "\ttype: "+token.type+"\tvalue: "+token.value
        return tokens
