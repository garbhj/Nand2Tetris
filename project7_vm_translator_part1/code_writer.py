class Writer(list):
    segments_map = {
        "local": "@LCL",
        "argument": "@ARG",
        "this": "@THIS",
        "that": "@THAT",
    }

    def __init__(self, file_name):
        super().__init__()
        self.include_comments = True
        self.comp_counter = 0
        self.file_name = file_name

    def write_line(self, parser):
        command_type, arg_1, arg_2 = parser.parse_line()
        print(command_type, arg_1, arg_2, sep="\n", end="\n\n")

        if self.include_comments:
            self.append(f"// {parser.current_command}")

        if command_type == "C_ARITHMETIC":
            return self.write_arithemetic(arg_1)
        elif command_type == "C_PUSH":
            return self.write_push(arg_1, int(arg_2))
        elif command_type == "C_POP":
            return self.write_pop(arg_1, int(arg_2))

    def write_arithemetic(self, command):
        if command in ["add", "sub", "and", "or"]:
            self.code_arithmetic(command)
        elif command in ["neg", "not"]:
            self.code_unary(command)
        elif command in ["lt", "eq", "gt"]:
            self.code_comparison(command)

    def code_arithmetic(self, command):
        """Two element logical & arithmetic operations: add, sub, and, and or"""
        op_map = {
            "add": "D+M",
            "sub": "M-D",  # Note: order matters
            "and": "D&M",
            "or": "D|M",
        }

        self.extend([
            "@SP",
            "AM=M-1",  # Decrement stack pointer one spot and move address to stack top
            "D=M",  # Set D to last value
            "A=A-1",  # Move pointer to second last value
            f"M={op_map[command]}"  # Perform operation in position
        ])

    def code_unary(self, command):
        """Single element operations: not and neg"""
        op_map = {
            "not": "!",
            "neg": "-"
        }

        self.extend([
            "@SP",
            "A=M-1",  # Do not decrement stack pointer
            f"M={op_map[command]}M"
        ])

    def code_comparison(self, command):
        """Comparison operations: lt, gt, and eq"""
        self.extend([
            "@SP",
            "AM=M-1",  # Decrement stack pointer one spot and move address to y (last)
            "D=M",
            "A=A-1",  # Move address to x (second last)
            "D=M-D",  # Calculate difference (x - y </=/> 0)
            "@SP",
            "A=M-1",
            "M=-1",  # Unconditional set to true (this is to save instructions)
            f"@COMP_END_{self.comp_counter}",
            f"D;J{command.upper()}",  # Leave as true and jump to end if condition is satisfied
            "@SP",
            "A=M-1",
            "M=0",  # Overwrite as false if condition is not satisfied
            f"(COMP_END_{self.comp_counter})"
        ])

        # Counter used to distinguish between ROM label symbols
        self.comp_counter += 1

    def write_push(self, segment, index):
        """
        Writes "Push" operation.
        :param segment: denotes memory segment
        :param index: index in segment
        """
        # Select address by register
        if segment in self.segments_map:
            self.extend([
                self.segments_map[segment],
                "D=M",   # Take the address of the register pointer
                f"@{index}",
                "A=D+A",  # And then add the index to get the address
                "D=M"  # Store address in D register
            ])
        elif segment == "constant":
            self.extend([
                f"@{index}",  # For constants, take the address, not the stored value
                "D=A"
            ])
        elif segment == "static":
            self.extend([
                f"@{self.file_name}.{index}",  # Use symbolic name; automatically start at 16.
                "D=M"
            ])
        elif segment == "pointer":
            if index not in (0, 1):
                raise ValueError("Pointer segment index must be 0 or 1")
            self.extend([
                f"@R{3 + index}",
                "D=M"
            ])
        elif segment == "temp":
            if not (0 <= index <= 7):
                raise ValueError("Temp segment index must be 0–7")
            self.extend([
                f"@R{5 + index}",
                "D=M"
            ])
        else:
            raise ValueError(f"Unknown segment for push command: {segment}")

        self.extend([
            "@SP",  # Store value in address
            "A=M",
            "M=D",
            "@SP",  # Increment SP
            "M=M+1"
        ])

    def write_pop(self, segment, index):
        """
        Writes "pop" operation.
        :param segment: denotes memory segment
        :param index: index in segment
        """
        if segment in self.segments_map:
            self.extend([
                self.segments_map[segment],
                "D=M",   # Take the address of the register pointer
                f"@{index}",
                "D=D+A",  # And then add the index to get the address
                "@R13",  # Store address in spare register
                "M=D",
                "@SP",
                "AM=M-1",  # Decrement stack pointer and move address to top element
                "D=M",  # Access top element
                "@R13",  # Move address register to previously calculated memory segment address
                "A=M",
                "M=D"  # Store that value
            ])
        elif segment == "static":
            self.extend([
                "@SP",
                "AM=M-1",  # Decrement stack pointer, move memory to top value
                "D=M",
                f"@{self.file_name}.{index}",  # Store value in symbolic variable
                "M=D"
            ])
        elif segment == "pointer":
            if index not in (0, 1):
                raise ValueError("Pointer segment index must be 0 or 1")
            self.extend([
                "@SP",
                "AM=M-1",  # Decrement stack pointer, move memory to top value
                "D=M",
                f"@{3 + index}",  # Store value in segment address
                "M=D"
            ])
        elif segment == "temp":
            if not (0 <= index <= 7):
                raise ValueError("Temp segment index must be 0–7")
            self.extend([
                "@SP",
                "AM=M-1",  # Decrement stack pointer, move memory to top value
                "D=M",
                f"@{5 + index}",  # Store value in address
                "M=D"
            ])
        else:
            raise ValueError(f"Unknown segment for push command: {segment}")






