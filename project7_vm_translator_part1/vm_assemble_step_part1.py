import os
from project6_assembler.assembler import Assembler


def run_project7_translation():
    # Get current directory (in current package)
    here = os.path.dirname(__file__)
    input_dir = os.path.join(here, "asm")
    output_dir = os.path.join(here, "hack")
    os.makedirs(output_dir, exist_ok=True)  # Create directory if not exist

    files = ["BasicTest", "PointerTest", "SimpleAdd", "StackTest", "StaticTest"]
    for file in files:
        assembler = Assembler(file, input_dir=input_dir, output_dir=output_dir)
        assembler.assemble()
        assembler.write_hack(file)


if __name__ == "__main__":
    run_project7_translation()
