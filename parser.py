from tokenizer import Tokenizer
from syntax_analysis import SyntaxAnalysis
import argparse

parser = argparse.ArgumentParser(description="Parser of basicDTD language")
parser.add_argument('--input', help='Text to be parsed', type=str)
args = parser.parse_args()

#input_string = args.input
input_string = "<!ELEMENT _%HelloWorld%_ (#PCDATA) > <!ATTLIST Ahoj hulahej IDREF #REQUIRED>"

if input_string:
    print "\tYou have specified this as an input: \n" + input_string + '\n'
    tokenizer = Tokenizer()
    tokens = tokenizer.tokenizeInput(input_string)
    analyzer = SyntaxAnalysis()
    analyzer.initializeParseTable()
    analyzer.analyzeTokens(tokens)


# Sentences examples
#
# <!ATTLIST Ahoj bla1_D CDATA #REQUIRED>
# <!ELEMENT _ahoj-cau. EMPTY>
# <!ATTLIST :merry^Christmas&PF%2017 Santa:Claus NMTOKEN #IMPLIED Jingl_Bells IDREF #REQUIRED>
# <!ELEMENT Morho-detvo-mojho-rodu ANY>
# <!ELEMENT _%HelloWorld%_ (#PCDATA) > <!ATTLIST Ahoj hulahej IDREF #REQUIRED>    ERROR
# <!ELEMENT I_LOVE_FIIT^^ ( ( or_not ? ) )>  ERROR
# <!ELEMENT Winter.is.coming. ( ( ( valar * | dohaeris * ) + ) )>
# <!ATTLIST Waar kom ( je | u ) #FIXED "vandaan.">
# <!ATTLIST Strc _2_prsty ( skrz ) "krk">
# <!ELEMENT word ( ( word , word , word ) * )>

