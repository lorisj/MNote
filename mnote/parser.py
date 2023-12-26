from lark import Lark
from lark.indenter import Indenter

block_grammer = r"""
    start: (content | section_name)*

    section_name: _WS* "#" /[^%\n]+/ _NL?

    content: (text | block)

    block: (definition | result | example | proof | claim)

    claim: _WS* ("%clm(" BLOCKNAME ")") (blockname_array)? _WS*_NL [_INDENT content* _DEDENT]
    result: _WS* ("%res(" BLOCKNAME ")") (blockname_array)? _WS*_NL [_INDENT content* _DEDENT] 
    example: _WS*  ("%exp(" BLOCKNAME ")") (blockname_array)? _WS*_NL [_INDENT content* _DEDENT]
    definition: _WS*  ("%def(" BLOCKNAME ")")(blockname_array)? _WS*_NL [_INDENT content* _DEDENT]
    proof: _WS* ("%pf") _WS* _NL [_INDENT content* _DEDENT]

    blockname_array: "["BLOCKNAME (","_WS* BLOCKNAME)* "]"
"""


# Text grammar, i.e. simplifying LaTeX structure.
text_grammar = r"""
    text: (line | tex_block | empty_line | line_command) +

    line_command: (dline | subtitle | image | todoline | newpage)_WS* _NL?
    line: (_WS* STRING inline_command? STRING?  _NL?)  
    inline_command: block_reference | bib_reference
    block_reference: _WS* "%ref(" BLOCKNAME ")" _WS*
    bib_reference: _WS* "%bib(" BLOCKNAME ")" _WS*
    
    empty_line: _WS* _NL
    tex_block: enumerate | itemize | nice_equation | equation | tikcd | tikcd_center
    enumerate:_WS* "%enum" _WS* _NL [_INDENT item+ _DEDENT]
    tikcd: _WS* "%cd" _WS* _NL [_INDENT text _DEDENT]    
    tikcd_center: _WS* "%ccd" _WS* _NL [_INDENT text _DEDENT]
    itemize: _WS*"%item" _WS? _NL [_INDENT item+ _DEDENT]
    nice_equation: _WS*"%neq" _WS*_NL [_INDENT text _DEDENT]
    equation: _WS*"%eq" _WS* _NL [_INDENT text _DEDENT]
    item: "%i" _WS? content*
    
    dline: _WS* "%dl"
    newpage: _WS* "%np"
    subtitle: _WS* "%st(" BLOCKNAME ")" 
    todoline: _WS* "%todo" STRING 
    image: _WS* "%img(" BLOCKNAME ")" _WS*
    
"""

# Need the ? in _NL? to handle the case where there is no newline at the end of the file.


symbol_grammar =r"""
    STRING:  /[^%#\n]+/
    _WS: /[\t ]+/
    BLOCKNAME: /[a-zA-Z0-9][a-zA-Z0-9_ "\-.]*/
    %declare _INDENT _DEDENT
    _NL: /(\r?\n[\t ]*)/
    filepath: /\/?([a-zA-Z0-9\-\.\/_]+)\.\w{1,4}/
    link: /(http(s)?:\/\/)?(www\.)?[a-zA-Z0-9\-\.]+/ filepath
"""

full_grammar = block_grammer + text_grammar + symbol_grammar


class TreeIndenter(Indenter):
    NL_type = '_NL'
    OPEN_PAREN_types = []
    CLOSE_PAREN_types = []
    INDENT_type = '_INDENT'
    DEDENT_type = '_DEDENT'
    tab_len = 4


def get_parser():
    return Lark(full_grammar, parser='lalr', postlex=TreeIndenter())
