from project8_vm_translator_part2.parser import Parser
from project8_vm_translator_part2.code_writer import Writer
import os
from pathlib import Path


class VMTranslator:
    """
    Accepts either a .vm file or directory of .vm files, and generates a single .asm file.
    """
    def __init__(self, input_path, output_path=None):
        """
        input_path: path to a single .vm file or a directory of .vm files
        output_path: path to output .asm file OR directory
        """
        self.input_path = Path(input_path)
        self.input_is_directory = self.input_path.is_dir()

        # Handle different cases for output path
        if output_path:
            output_path = Path(output_path)
            if output_path.is_dir():
                # If output path is a directory, put output file inside with same name stem as input
                self.output_path = output_path / f"{self.input_path.stem}.asm"  # output/path/inputStem.asm
            else:  # If explicitly given output file
                self.output_path = output_path
        else:
            # If unspecified, store in same directory as input with .asm suffix
            self.output_path = self.input_path.with_suffix(".asm")

        self.writer = Writer()  # Just one writer, as all files in a directory end up in the same .asm file.

    def translate(self):
        """Translate a single file or all .vm files in a directory"""
        vm_files = self._get_vm_files()

        # Initialize Sys.m
        if self.input_is_directory:
            self.writer.write_init()

        print(f"\nPath: {self.input_path}")

        for file in vm_files:
            file_name = file.stem  # Base name without extension
            self.writer.set_file_name(file_name)
            print(f"Translating {file_name}")

            vm_code = self.read(file)
            parser = Parser(vm_code)

            while parser.has_next():
                parser.advance()
                self.writer.write_line(parser)

    def _get_vm_files(self):
        """Returns list of .vm files from input path"""
        # If input is a single file, use that.
        if self.input_path.is_file() and self.input_path.suffix == ".vm":
            return [self.input_path]

        # If input is a directory, return all the .vm files in that directory.
        if self.input_path.is_dir():
            return list(self.input_path.glob("*.vm"))  # Note: glob = name matching in directory

        raise FileNotFoundError(f"No .vm files found at {self.input_path}")

    @staticmethod
    def read(file_path):
        """Returns cleaned contents of specified file"""
        with open(file_path) as f:
            return VMTranslator.clean(f.readlines())

    def write(self, file_path = None):
        """Writes translated asm code to new file"""
        if file_path is None:
            file_path = self.output_path

        os.makedirs(os.path.dirname(file_path), exist_ok=True)  # In case output directory doesn't exist
        with open(file_path, "w") as f:
            for line in self.writer:
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
    files = [
        "files/BasicLoop/BasicLoop.vm",
        "files/FibonacciSeries/FibonacciSeries.vm",
        "files/SimpleFunction/SimpleFunction.vm",
        "files/FibonacciElement",
        "files/NestedCall",
        "files/StaticsTest"
    ]

    output_dir = "files/asm"

    for file in files:
        translator = VMTranslator(file, output_dir)
        translator.translate()
        translator.write()


if __name__ == "__main__":
    run()