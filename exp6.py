import re

class CodeGenerator:
    def __init__(self):
        self.register = "R1"
        self.output = []

    def generate(self, tac_lines):
        for line in tac_lines:
            match = re.match(r"(\w+)\s*=\s*(\w+)\s*([\+\-\*/])\s*(\w+)", line)
            if match:
                dest, op1, operator, op2 = match.groups()
                self.output.append(f"LOAD {self.register}, {op1}")
                asm_op = self.get_asm_operator(operator)
                self.output.append(f"{asm_op} {self.register}, {op2}")
                self.output.append(f"MOV {dest}, {self.register}")
            else:
                # Handle simple assignments like t1 = x
                match = re.match(r"(\w+)\s*=\s*(\w+)", line)
                if match:
                    dest, src = match.groups()
                    self.output.append(f"LOAD {self.register}, {src}")
                    self.output.append(f"MOV {dest}, {self.register}")

        return self.output

    def get_asm_operator(self, op):
        return {
            '+': 'ADD',
            '-': 'SUB',
            '*': 'MUL',
            '/': 'DIV'
        }.get(op, 'UNKNOWN')

# --- Example ---
tac_code = [
    "t1 = a + b",
    "t2 = t1 * c",
    "t3 = t2 - d"
]

gen = CodeGenerator()
assembly = gen.generate(tac_code)

print("Generated Code:")
for line in assembly:
    print("  ", line)
