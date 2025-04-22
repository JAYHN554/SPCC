import re

class ThreeAddressCodeGenerator:
    def __init__(self):
        self.temp_count = 0
        self.code = []

    def new_temp(self):
        self.temp_count += 1
        return f"t{self.temp_count}"

    def generate(self, expression):
        tokens = self.tokenize(expression)
        postfix = self.infix_to_postfix(tokens)
        result = self.postfix_to_TAC(postfix)
        return self.code, result

    def tokenize(self, expr):
        return re.findall(r'[a-zA-Z_]\w*|\d+|[-+*/()]', expr)

    def infix_to_postfix(self, tokens):
        # Shunting-yard algorithm
        precedence = {'+':1, '-':1, '*':2, '/':2}
        output = []
        stack = []

        for token in tokens:
            if re.match(r'[a-zA-Z_]\w*|\d+', token):  # operand
                output.append(token)
            elif token in precedence:
                while (stack and stack[-1] in precedence and
                       precedence[token] <= precedence[stack[-1]]):
                    output.append(stack.pop())
                stack.append(token)
            elif token == '(':
                stack.append(token)
            elif token == ')':
                while stack and stack[-1] != '(':
                    output.append(stack.pop())
                stack.pop()  # remove '('
        while stack:
            output.append(stack.pop())
        return output

    def postfix_to_TAC(self, postfix):
        stack = []
        for token in postfix:
            if re.match(r'[a-zA-Z_]\w*|\d+', token):  # operand
                stack.append(token)
            else:  # operator
                b = stack.pop()
                a = stack.pop()
                temp = self.new_temp()
                self.code.append(f"{temp} = {a} {token} {b}")
                stack.append(temp)
        return stack[-1]  # final result temp

# --- Example ---
expr = "a + b * c - d"
tac_gen = ThreeAddressCodeGenerator()
tac_code, result = tac_gen.generate(expr)

print("Three-Address Code:")
for line in tac_code:
    print("  ", line)
print("\nResult stored in:", result)
