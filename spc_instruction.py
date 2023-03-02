class SPCInstruction:
    def __init__(self, instruction, hex_code, required_bytes):
        self.instruction = instruction
        self.hex_code = hex_code
        self.required_bytes = required_bytes

    def __str__(self):
        return f"{self.instruction} | {self.hex_code} | {self.required_bytes}"

