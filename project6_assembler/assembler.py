from project6_assembler.symbol_table import SymbolTable
from project6_assembler.parser import Parser


class Assembler:
    def __init__(self, file, input_dir="asm", output_dir="hack"):
        self.input_dir = input_dir
        self.output_dir = output_dir

        with open(f"{self.input_dir}/{file}.asm", "r") as f:
            asm_lines = f.readlines()

        self.table = SymbolTable()
        self.parser = Parser()
        self.instructions = asm_lines
        self.assembled_program = []

    def assemble(self):
        self.clean()
        self.extract_labels()
        # print(self.table)
        self.assembled_program = self.translate()
        return self.assembled_program

    def clean(self):
        """Removes comments and whitespace."""
        cleaned = []
        for line in self.instructions:
            inst = line.strip().split("/")[0].strip()
            if not inst == "":
                cleaned.append(inst)
        self.instructions = cleaned

    def extract_labels(self):
        """Adds all labels (ADDRESS) to the symbol table, and removes them from the code itself."""
        index = 0
        labels_removed = []  # All instructions excluding labels
        for instruction in self.instructions:
            if instruction[0] == "(":
                self.table.add(instruction[1:-1], index)
                # Do not increment index if at a label, as labels are removed for second pass.
            else:
                index += 1
                labels_removed.append(instruction)
        self.instructions = labels_removed

    def translate(self):
        """Translates the instructions (second pass)"""
        n = 16
        assembled_program = []
        for instruction in self.instructions:

            if instruction[0] == "@":  # A-instructions
                symbol = instruction[1:]
                address = self.table.get(symbol)
                if symbol.isnumeric():
                    address = symbol
                elif address == -1:
                    self.table.add(symbol, n)
                    address = n
                    n += 1
                assembled_instruction = self.parser.a_inst(address)
            else:
                assembled_instruction = self.parser.c_inst(instruction)
            assembled_program.append(assembled_instruction)
        return assembled_program

    def write_hack(self, file):
        with open(f"{self.output_dir}/{file}.hack", "w") as f:
            for line in self.assembled_program:
                f.write(line + "\n")


def run(files, input_dir="asm", output_dir="hack"):

    for file in files:
        assembler = Assembler(file, input_dir, output_dir)
        assembler.assemble()
        assembler.write_hack(file)


if __name__ == "__main__":
    run(["add", "max", "maxl", "rect", "rectl", "pong", "pongl"])