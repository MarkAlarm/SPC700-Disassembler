import instruction

if __name__ == '__main__':
    file = open("raw-bytes.txt", 'r')
    raw_bytes = file.readline().split(' ')
    file.close()

    file = open("opcodes.csv", 'r')

    instructions = []

    for line in file.readlines():
        temp = line.strip().split('|')
        instructions.append(instruction.Instruction(temp[0], temp[1], temp[2]))

    file.close()

    instructions.pop(0)

    instructions.sort(key=lambda x: int(x.hex_code, 16))

    byte_index = 0

    while byte_index < len(raw_bytes):
        instruction_byte = int(raw_bytes[byte_index], 16)

        print(instructions[instruction_byte].opcode)
        byte_index += int(instructions[instruction_byte].required_bytes)

