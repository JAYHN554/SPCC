 #LL1_table

LL1_table = {
    ('E', 'id'): ['T', 'E\''],
    ('E', '('): ['T', 'E\''],
    ('E\'', '+'): ['+', 'T', 'E\''],
    ('E\'', ')'): [],
    ('E\'', '$'): [],
    ('T', 'id'): ['F', 'T\''],
    ('T', '('): ['F', 'T\''],
    ('T\'', '+'): [],
    ('T\'', '*'): ['*', 'F', 'T\''],
    ('T\'', ')'): [],
    ('T\'', '$'): [],
    ('F', 'id'): ['id'],
    ('F', '('): ['(', 'E', ')'],
}

def ll1_parse(tokens):
    tokens.append('$')
    stack = ['$', 'E']
    i = 0
    while stack:
        top = stack.pop()
        current = tokens[i]
        if top == current:
            i += 1
        elif top in {'id', '+', '*', '(', ')', '$'}:
            return False
        elif (top, current) in LL1_table:
            production = LL1_table[(top, current)]
            for symbol in reversed(production):
                stack.append(symbol)
        else:
            return False
    return i == len(tokens)

# Test
tokens = ['id', '+', 'id', '*', 'id']
print("Accepted" if ll1_parse(tokens) else "Rejected")
