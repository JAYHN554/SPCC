import re

# Define token types and patterns
token_specification = [
    ('NUMBER',    r'\d+(\.\d*)?'),      # Integer or decimal number
    ('ID',        r'[A-Za-z_]\w*'),     # Identifiers
    ('ASSIGN',    r'='),                # Assignment operator
    ('EQ',        r'=='),               # Equality operator
    ('OP',        r'[+\-*/]'),          # Arithmetic operators
    ('LPAREN',    r'\('),               # Left Parenthesis
    ('RPAREN',    r'\)'),               # Right Parenthesis
    ('LBRACE',    r'\{'),               # Left brace
    ('RBRACE',    r'\}'),               # Right brace
    ('SEMI',      r';'),                # Semicolon
    ('NEWLINE',   r'\n'),               # Line endings
    ('SKIP',      r'[ \t]+'),           # Skip spaces and tabs
    ('COMMENT',   r'//.*'),             # Single line comment
    ('MISMATCH',  r'.'),                # Any other character
]

# Compile regex patterns
tok_regex = '|'.join(f'(?P<{name}>{pattern})' for name, pattern in token_specification)
keywords = {'if', 'else', 'while', 'for', 'int', 'float', 'return'}

def lexical_analyzer(code):
    tokens = []
    line_num = 1

    for mo in re.finditer(tok_regex, code):
        kind = mo.lastgroup
        value = mo.group()

        if kind == 'NUMBER':
            tokens.append(('NUMBER', value))
        elif kind == 'ID':
            if value in keywords:
                tokens.append(('KEYWORD', value))
            else:
                tokens.append(('IDENTIFIER', value))
        elif kind == 'ASSIGN':
            tokens.append(('ASSIGN', value))
        elif kind == 'EQ':
            tokens.append(('EQ', value))
        elif kind == 'OP':
            tokens.append(('OPERATOR', value))
        elif kind in {'LPAREN', 'RPAREN', 'LBRACE', 'RBRACE', 'SEMI'}:
            tokens.append((kind, value))
        elif kind == 'NEWLINE':
            line_num += 1
        elif kind == 'SKIP' or kind == 'COMMENT':
            continue
        elif kind == 'MISMATCH':
            raise RuntimeError(f'Unexpected character {value!r} on line {line_num}')
    
    return tokens
code = '''
int x = 10;
if (x == 10) {
    x = x + 1;
    // Increment x
}
'''

tokens = lexical_analyzer(code)
for token in tokens:
    print(token)
