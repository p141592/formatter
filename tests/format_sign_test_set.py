from parser.tree.raw_nodes import BlankLine, RawLine

raw_line = lambda x: RawLine(offset=0, source=x)

FORMAT_SIGN = (
    (BlankLine(offset=0), False),
    (raw_line('=========='), True),
    (raw_line('**************'), True),
    (raw_line('**Syntax Notes:** In this and the following chapters, extended BNF'), True),
    (raw_line('   name ::= othername'), True),
    (raw_line('* otherwise, if either argument is a floating point number, the'), True),
    (raw_line('''left argument to the '%' operator).  Extensions must define their own'''), False),
    (raw_line('--------------------------'), True),
    (raw_line('6.2.1. Identifiers (Names)'), False),
    (raw_line('inserted, in front of the name.  For example, the identifier "__spam"'), False),
    (raw_line('literals:'), False),
    (raw_line('   parenth_form ::= "(" [starred_expression] ")"'), True),
    (raw_line('parentheses *are* required --- allowing unparenthesized "nothing" in'), False),
    (raw_line('  **PEP 342** - Coroutines via Enhanced Generators'), True),
    (raw_line('   comparison'), True),
    (raw_line('This is the MIT license: `<http://www.opensource.org/licenses/mit-license.php>`_'), True)
)