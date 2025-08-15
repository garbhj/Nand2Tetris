from project6_assembler.code import Code

class Parser:
    """
    Parses cleaned instructions, one instruction at a time.
    """
    def __init__(self):
        self.code = Code()

    def a_inst(self, address):
        return self.code.a_encode(address)

    def c_inst(self, instruction):
        """Decomposes and returns relevant parts of a C instruction"""
        # destination is the part before the equal sign, if it exists
        dest = ""
        if "=" in instruction:
            dest = instruction.split("=")[0]
        # comparison always exists, and is between the equal sign and semicolon (if present)
        comp = instruction.split("=")[-1].split(";")[0]
        # jump after the semicolon, if it exists
        jump = ""
        if ";" in instruction:
            jump = instruction.split(";")[-1]
        return self.code.c_encode(comp, dest, jump)


