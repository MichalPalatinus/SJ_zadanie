# basic_DTD_parser

BNF (Backus-Naur Form) of basicDTD:

    dtddocument ::= declaration {declaration} .  
    declaration ::= attrdecl | elemdecl .  
    elemdecl ::= '<!ELEMENT' name ('EMPTY' | 'ANY' | '(#PCDATA)' | elemchild) '>' .  
    elemchild ::= '(' (choice | seq)['?' | '*' | '+'] ')' .  
    choice ::= '(' cp ['|' cp] ')' .  
    seq ::= '(' cp {',' cp} ')' .  
    cp ::= (name | choice | seq) ['?' | '*' | '+'] .  
    attrdecl ::= '<!ATTLIST' name {name attrtype defaultdecl} '>' .  
    attrtype ::= 'CDATA' | 'NMTOKEN' | 'IDREF' | '(' word ['|' word] ')' . defaultdecl ::= '#REQUIRED' | '#IMPLIED' | (['#FIXED'] '"' word {word} '"' ) .  
    name ::= (letter | '_' | ':') {namechar} .  
    namechar ::= letter | digit | '.' | '-' | '_' | ':' .  
    letter ::='A'|..|'Z'|'a'|..|'z'.  
    number ::= digit {digit} .  
    digit ::= '0' | .. | '9' .  
    word ::= char {char} .  
    char ::= letter | digit | '%' | '&' | '^' .

BNF grammar transformed into LL(1) grammar (rules form):

    DTDOC -> '<' DECLARATION L
    L -> DTDOC | ε
    DECLARATION -> ATTLIST WORD Z '>' | ELEMENT WORD X '>'
    X -> EMPTY| ANY | PCDATA | '(' F ')'
    F -> '(' CP K Y
    Y -> '?' | '*' | '+' | ε
    H -> ',' CP H | ε
    K -> ')' | '|' CP ')' | ',' CP H ')'
    CP -> WORD Y | '(' CP K Y
    Z -> WORD ATTRTYPE DEFAULTDECL Z | ε
    ATTRTYPE -> CDATA | NMTOKEN | IDREF | '(' WORD E ')'
    E -> '|' WORD | ε
    DEFAULTDECL -> REQUIRED | IMPLIED | J '"' WORD B '"'
    J -> FIXED | ε
    B -> WORD B | ε

Note that the grammar (in BNF) had to be slightly modified in order to transform it into a LL(1) grammar (e.g., merging rules *name* and *word* together).

##Usage
1. Single sentence: `python parser.py '<!ELEMENT integer ((bool,string,float)*)>'`
2. Multiple sentences: `python parser.py '<!ELEMENT integer ((bool,string,float)*)> <!ELEMENT integer ((bool,string,float)*)>'`
3. Help: `python parser.py -h`
