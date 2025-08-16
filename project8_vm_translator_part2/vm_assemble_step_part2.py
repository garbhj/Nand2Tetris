import os
from project6_assembler.assembler import Assembler


def run_project8_translation():
    # Get current directory and relative directories
    here = os.path.dirname(__file__)
    input_dir = os.path.join(here, "files/asm")
    output_dir = os.path.join(here, "files/hack")
    os.makedirs(output_dir, exist_ok=True)  # make directory if not exist

    files = ["BasicLoop", "FibonacciSeries", "FibonacciElement", "NestedCall", "SimpleFunction", "StaticsTest"]
    for file in files:
        assembler = Assembler(file, input_dir=input_dir, output_dir=output_dir)
        assembler.assemble()
        assembler.write_hack(file)


if __name__ == "__main__":
    run_project8_translation()
