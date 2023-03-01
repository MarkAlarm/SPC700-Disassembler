class Instruction:
    def __init__(self, opcode, hex_code, required_bytes):
        self.opcode = opcode
        self.hex_code = hex_code
        self.required_bytes = required_bytes

    def __str__(self):
        return f"{self.opcode} | {self.hex_code} | {self.required_bytes}"

