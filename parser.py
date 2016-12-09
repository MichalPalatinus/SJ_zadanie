from tokenizer import Tokenizer
from syntax_analysis import SyntaxAnalysis
import argparse
from token import Token

parser = argparse.ArgumentParser(description="Parser of basicDTD language")
parser.add_argument('--input', help='Text to be parsed', type=str)
args = parser.parse_args()

#input_string = args.input
input_string = "<!ATTLIST Ahoj bla1_D CDATA #REQUIRED> <!ELEMENT _ahoj-cau. EMPTY>"

if input_string:
    print "\tYou have specified this as an input: \n" + input_string + '\n'
    tokenizer = Tokenizer()
    tokens = tokenizer.tokenizeInput(input_string)
    tokens.append(Token("EOF", "$"))
    analyzer = SyntaxAnalysis()
    analyzer.initializeParseTable()
    analyzer.analyzeTokens(tokens)


# Sentences examples
#
# OK <!ATTLIST Ahoj bla1_D CDATA #REQUIRED>
# OK <!ELEMENT _ahoj-cau. EMPTY>
# OK <!ATTLIST :merry^Christmas&PF%2017 Santa:Claus NMTOKEN #IMPLIED Jingl_Bells IDREF #REQUIRED>
# OK <!ELEMENT Morho-detvo-mojho-rodu ANY>
# OK <!ELEMENT from (#PCDATA)> <!ATTLIST Ahoj hulahej IDREF #REQUIRED>
# OK <!ELEMENT I_LOVE_FIIT^^ ( ( or_not ? ) )>
# OK <!ELEMENT Winter.is.coming. ( ( ( valar * | dohaeris * ) + ) )>
# OK <!ATTLIST Waar kom ( je | u ) #FIXED \" vandaan \">
# OK <!ATTLIST Strc _2_prsty ( skrz ) \" krk \">
# OK <!ELEMENT integer ( ( bool , string , float ) * )>
# "<!ATTLIST Ahoj bla1_D CDATA #REQUIRED> !ELEMENT _ahoj-cau. EMPTY> <!ATTLIST :merry^Christmas&PF%2017 Santa:Claus NMTOKEN #IMPLIED Jingl_Bells IDREF #REQUIRED> <!ELEMENT Morho-detvo-mojho-rodu ANY> <!ELEMENT from (#PCDATA)> <!ATTLIST Ahoj hulahej IDREF #REQUIRED> <!ELEMENT I_LOVE_FIIT^^ ( ( or_not ? ) )> <!ATTLIST Waar kom ( je | u ) #FIXED \" vandaan \"> <!ATTLIST Strc _2_prsty ( skrz ) \" krk \"> <!ELEMENT integer ( ( bool , string , float ) * )>"

