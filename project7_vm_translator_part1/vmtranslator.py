from project7_vm_translator_part1.parser import Parser
from project7_vm_translator_part1.code_writer import Writer


class VMTranslator:
    def __init__(self, files):
        self.files = files

    def translate(self):
        for file in self.files:
            writer = Writer(file)
            vm_code = self.read(file)
            parser = Parser(vm_code)

            while parser.has_next():
                parser.advance()
                writer.write_line(parser)

            self.write(writer, f"asm/{file}.asm")

    @staticmethod
    def read(file_path):
        """Returns cleaned contents of specified file"""
        with open(f"vm/{file_path}.vm") as f:
            return VMTranslator.clean(f.readlines())

    @staticmethod
    def write(translated_code, file_path="asm/unnamed.asm"):
        """Writes translated asm code to new file"""
        with open(file_path, "w") as f:
            for line in translated_code:
                f.write(line + "\n")

    @staticmethod
    def clean(instructions):
        """Removes comments and whitespace"""
        cleaned = []
        for line in instructions:
            inst = line.strip().split("/")[0].strip()
            if not inst == "":
                cleaned.append(inst)
        return cleaned


def run():
    """
    Translates all the files
    """
    files = ["BasicTest", "PointerTest", "SimpleAdd", "StackTest", "StaticTest"]

    translator = VMTranslator(files)
    translator.translate()


if __name__ == "__main__":
    run()