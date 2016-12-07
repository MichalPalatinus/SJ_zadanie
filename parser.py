from tokenizer import Tokenizer
from syntax_analysis import SyntaxAnalysis
import argparse

parser = argparse.ArgumentParser(description="Parser of basicDTD language")
parser.add_argument('--input', help='Text to be parsed', type=str)
args = parser.parse_args()

#input_string = args.input
input_string = "<!ATTLIST ahoj>"
if input_string:
    print "\tYou have specified this as an input: \n" + input_string + '\n'
    tokenizer = Tokenizer()
    tokens = tokenizer.tokenizeInput(input_string)
    analyzer = SyntaxAnalysis()
    analyzer.initializeParseTable()
    analyzer.analyzeTokens(tokens)
