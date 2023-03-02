import spc_instruction

if __name__ == '__main__':
    file = open("opcodes.csv", 'r')
    spc_instructions = []

    for line in file.readlines():
        temp = line.strip().split('|')
        spc_instructions.append(spc_instruction.SPCInstruction(temp[0], temp[1], temp[2]))
    file.close()

    spc_instructions.pop(0)
    spc_instructions.sort(key=lambda x: int(x.hex_code, 16))

    file = open("mmx-engine.txt", 'r')
    spc_engine = file.readline().split(' ')
    file.close()

    spc_index = 0
    while spc_index < len(spc_engine):
        spc_instruction = spc_instructions[int(spc_engine[spc_index], 16)]
        required_bytes = int(spc_instruction.required_bytes)
        formatted_instruction = str(spc_instruction.instruction)
        printed_raw_bytes = spc_engine[spc_index]

        # one operand
        if required_bytes == 2:
            formatted_instruction = formatted_instruction.replace("<d>", f"${spc_engine[spc_index + 1]}")
            formatted_instruction = formatted_instruction.replace("<i>", f"#${spc_engine[spc_index + 1]}")
            printed_raw_bytes += " " + spc_engine[spc_index + 1]

        # two operands
        elif required_bytes == 3:
            formatted_instruction = formatted_instruction.replace("<a>", f"${spc_engine[spc_index + 2]}"
                                                                         f"{spc_engine[spc_index + 1]}")
            formatted_instruction = formatted_instruction.replace("<d1>", f"${spc_engine[spc_index + 1]}")
            formatted_instruction = formatted_instruction.replace("<d2>", f"${spc_engine[spc_index + 2]}")
            formatted_instruction = formatted_instruction.replace("<d>", f"${spc_engine[spc_index + 1]}")
            formatted_instruction = formatted_instruction.replace("<i>", f"#${spc_engine[spc_index + 2]}")
            printed_raw_bytes += " " + spc_engine[spc_index + 1] + " " + spc_engine[spc_index + 2]

        printed_address = str(hex(0x02C0 + spc_index).upper().replace('X','x') + ':').ljust(6, ' ')
        printed_instruction = formatted_instruction.ljust(13, ' ')
        printed_raw_bytes = printed_raw_bytes.ljust(8, ' ')

        print(f"{printed_address} | {printed_instruction} | {printed_raw_bytes}")
        spc_index += required_bytes


