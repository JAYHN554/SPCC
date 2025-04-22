import re

# Opcodes for the instruction set
OPCODES = {
    'LOAD': '01',
    'STORE': '02',
    'ADD': '03',
    'SUB': '04',
    'JMP': '05',
    'HLT': 'FF'
}

# Simulate registers (assume R1 = 1, R2 = 2, etc.)
REGISTER_MAP = {
    'R0': '0',
    'R1': '1',
    'R2': '2'
}

def parse_line(line):
    line = line.strip()
    if ':' in line:
        label, rest = line.split(':', 1)
        return label.strip(), rest.strip()
    return None, line

def pass_one(lines):
    symbol_table = {}
    address = 0
    for line in lines:
        label, instruction = parse_line(line)
        if label:
            symbol_table[label] = address
        if instruction and not instruction.startswith('.'):
            address += 1
    return symbol_table

def pass_two(lines, symbol_table):
    machine_code = []
    for line in lines:
        _, instruction = parse_line(line)
        if not instruction:
            continue
        tokens = instruction.split()
        if tokens[0] == '.DATA':
            data_value = tokens[1]
            machine_code.append(f'{int(data_value):02X}')
        elif tokens[0] in OPCODES:
            opcode = OPCODES[tokens[0]]
            if tokens[0] == 'HLT':
                machine_code.append(opcode + '00')
            elif len(tokens) == 3:
                reg = REGISTER_MAP[tokens[1].replace(',', '')]
                addr = symbol_table[tokens[2]]
                machine_code.append(f'{opcode}{reg}{addr:02X}')
            elif len(tokens) == 2:
                addr = symbol_table[tokens[1]]
                machine_code.append(f'{opcode}{addr:02X}')
    return machine_code

# --- Main ---
assembly_code = [
    "START:  LOAD R1, NUM",
    "        ADD R1, ONE",
    "        STORE R1, NUM",
    "        JMP START",
    "NUM:    .DATA 0",
    "ONE:    .DATA 1",
    "        HLT"
]

symbol_table = pass_one(assembly_code)
machine_code = pass_two(assembly_code, symbol_table)

print("Symbol Table:", symbol_table)
print("Machine Code:")
for code in machine_code:
    print(code)
