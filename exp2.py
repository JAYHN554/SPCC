def pass_one(lines):
    MNT = {}   # Macro Name Table
    MDT = []   # Macro Definition Table
    ALA = {}   # Argument List Array
    in_macro = False
    macro_name = ""
    ala_index = 1

    i = 0
    while i < len(lines):
        line = lines[i].strip()
        if line == "MACRO":
            in_macro = True
            i += 1
            header = lines[i].strip()
            parts = header.split()
            macro_name = parts[0]
            args = [arg.replace('&', '') for arg in parts[1:]]
            MNT[macro_name] = len(MDT)
            ALA[macro_name] = args
            MDT.append(f"{macro_name} {' '.join(args)}")  # Header in MDT
        elif line == "MEND":
            MDT.append("MEND")
            in_macro = False
        elif in_macro:
            # Replace &args with #index
            for idx, arg in enumerate(ALA[macro_name]):
                line = line.replace(f"&{arg}", f"#{idx}")
            MDT.append(line)
        i += 1
    return MNT, MDT, ALA

def pass_two(lines, MNT, MDT, ALA):
    output = []
    skip_macro = False

    for i in range(len(lines)):
        line = lines[i].strip()
        if line == "MACRO":
            skip_macro = True
        elif line == "MEND":
            skip_macro = False
        elif skip_macro:
            continue
        else:
            tokens = line.split()
            if tokens and tokens[0] in MNT:
                macro_name = tokens[0]
                args = tokens[1:]
                arg_map = {f"#{idx}": val for idx, val in enumerate(args)}
                start = MNT[macro_name] + 1
                for j in range(start, len(MDT)):
                    if MDT[j] == "MEND":
                        break
                    exp_line = MDT[j]
                    for key, val in arg_map.items():
                        exp_line = exp_line.replace(key, val)
                    output.append(exp_line)
            else:
                output.append(line)
    return output

# --- Main ---
macro_code = [
    "MACRO",
    "INCR &ARG",
    "    LOAD &ARG",
    "    ADD ONE",
    "    STORE &ARG",
    "MEND",
    "START",
    "INCR NUM",
    "HLT",
    "NUM: .DATA 0",
    "ONE: .DATA 1"
]

mnt, mdt, ala = pass_one(macro_code)
expanded_code = pass_two(macro_code, mnt, mdt, ala)

print("MNT:", mnt)
print("MDT:")
for line in mdt:
    print(" ", line)
print("\nExpanded Code:")
for line in expanded_code:
    print(" ", line)
