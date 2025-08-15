from project8_vm_translator_part2.parser import Parser
from project8_vm_translator_part2.code_writer import Writer
import os


class VMTranslator:
    """
    Accepts either a .vm file or directory of .vm files, and generates a single .asm file.
    """
    def __init__(self, input_path, output_path=None):
        """
        input_path: path to a single .vm file or a directory of .vm files
        output_path: path to output .asm file
        """
        self.input_path = input_path
        if output_path:
            self.output_path = output_path
        else:
            self.output_path = os.path.splitext(input_path)[0] + ".asm"

    def translate(self):
        """Translate a single file or all .vm files in a directory"""
        vm_files = self._get_vm_files()
        writer = Writer()  # Just one writer, as all files in a directory end up in the same .asm file.

        for file in vm_files:
            # Get raw file name without directory or extension
            file_name = os.path.splitext(os.path.basename(file))[0]
            writer.set_file_name(file_name)
            print(file_name)

            vm_code = self.read(file)
            parser = Parser(vm_code)

            # Iterate through the .vm file
            while parser.has_next():
                parser.advance()
                writer.write_line(parser)

            self.write(writer, self.output_path)

    def _get_vm_files(self):
        """Returns list of .vm files from input path"""
        # If input is a single file, use that.
        if os.path.isfile(self.input_path) and self.input_path.endswith(".vm"):
            return [self.input_path]

        # If input is a directory, return all the .vm files in that directory.
        if os.path.isdir(self.input_path):
            return [os.path.join(self.input_path, f) for f in os.listdir(self.input_path) if f.endswith(".vm")]

        raise FileNotFoundError(f"No .vm files found at {self.input_path}")

    @staticmethod
    def read(file_path):
        """Returns cleaned contents of specified file"""
        with open(file_path) as f:
            return VMTranslator.clean(f.readlines())

    @staticmethod
    def write(writer, file_path="asm/unnamed.asm"):
        """Writes translated asm code to new file"""
        os.makedirs(os.path.dirname(file_path), exist_ok=True)  # In case output directory doesn't exist
        with open(file_path, "w") as f:
            for line in writer:
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
    names = ["BasicLoop", "FibonacciElement", "FibonacciSeries", "NestedCall", "SimpleFunction", "StaticsTest"]

    for name in names:
        print("\nFolder:", name)
        input_path = os.path.join("files", name)
        translator = VMTranslator(input_path)
        translator.translate()


if __name__ == "__main__":
    run()