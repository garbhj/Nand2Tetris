class Writer(list):
    segments_map = {
        "local": "@LCL",
        "argument": "@ARG",
        "this": "@THIS",
        "that": "@THAT",
    }

    def __init__(self, file_name=None):
        super().__init__()
        self.include_comments = True
        self.comp_counter = 0
        self.file_name = file_name
        self.call_counter_by_function = {}
        self.current_function = None

    def set_file_name(self, file_name):
        self.file_name = file_name

    def write_init(self):
        # Writes the bootstrap code; sets SP = 256 and calls Sys.init
        self.extend(["@256", "D=A", "@SP", "M=D"])
        self.write_call("Sys.init", 0)

    def write_line(self, parser):
        command_type, arg_1, arg_2 = parser.parse_line()
        # print(command_type, arg_1, arg_2, sep="\n", end="\n\n")

        if self.include_comments:
            self.append(f"// {parser.current_command}")

        # Logic Commands
        if command_type == "C_ARITHMETIC":
            return self.write_arithemetic(arg_1)
        elif command_type == "C_PUSH":
            return self.write_push(arg_1, int(arg_2))
        elif command_type == "C_POP":
            return self.write_pop(arg_1, int(arg_2))

        # Branching Commands
        elif command_type in ["C_LABEL", "C_GOTO", "C_IF"]:
            return self.write_branching(command_type, arg_1)

        # Function Commands
        elif command_type in ["C_FUNCTION"]:
            return self.write_function(arg_1, int(arg_2))
        elif command_type == "C_CALL":
            return self.write_call(arg_1, int(arg_2))
        elif command_type == "C_RETURN":
            return self.write_return()

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

        # Place the value onto the stack
        self.extend([
            "@SP",  # Go to top of stack
            "A=M",
            "M=D",  # Place value
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
                f"@{5 + index}",  # Store value in segment address
                "M=D"
            ])
        else:
            raise ValueError(f"Unknown segment for push command: {segment}")

    def write_branching(self, command, label):
        # Ensure unique labels:
        # functionName.label to prevent label collisions between functions
        if self.current_function:
            label = f"{self.current_function}${label}"

        if command == "C_LABEL":
            self.append(f"({label})")  # Set label
        elif command == "C_GOTO":
            self.extend([
                f"@{label}",  # Unconditional jump to label
                "0;JMP"
            ])
        elif command == "C_IF":
            self.extend([
                "@SP",  # Pop top element
                "AM=M-1",
                "D=M",
                f"@{label}",  # Jump if popped element != 0 (i.e. not false)
                "D;JNE"
            ])

    def write_call(self, function, nArgs):
        # Determine return label by index
        count = self.call_counter_by_function.get(function, 0)
        return_label = f"{function}$ret.{count}"
        self.call_counter_by_function[function] = count + 1

        # Push return address of caller (label added at end)
        self.extend([f"@{return_label}", "D=A", "@SP", "A=M", "M=D", "@SP", "M=M+1"])

        # Push segment pointers of caller
        for segment in ("LCL", "ARG", "THIS", "THAT"):
            self.extend([f"@{segment}", "D=M", "@SP", "A=M", "M=D", "@SP", "M=M+1"])

        self.extend([
            # Repositions ARG to first argument = SP - 5(4 stored segments + 1 return address) - nArgs
            "@SP", "D=M", "@5", "D=D-A", f"@{nArgs}", "D=D-A", "@ARG", "M=D",

            # Repositions LCL to SP
            "@SP", "D=M", "@LCL", "M=D",

            # Jump to function
            f"@{function}", "0;JMP",
            
            # Add return address label
            f"({return_label})"
        ])

    def write_function(self, function, nVars):
        count = self.current_function = function

        # Note; self.write_push("constant", 0) isn't used for efficiency.
        self.extend([
            f"({function})",  # Create function label (Note: compiled bytecode already uses Xxx.funcName)
            "@SP", "A=M"  # Go to stack pointer
        ])
        for i in range(nVars):  # Add a zero for each local variable
            self.extend([
                "M=0", "A=A+1"
            ])
        self.extend([  # Update stack pointer to new location
            "D=A", "@SP", "A=M"
        ])

    def write_return(self):
        self.extend([
            # Stores LCL as end_frame address in R13 (as LCL will be changed)
            "@LCL",
            "D=M",
            "@R13",  # end_frame
            "M=D",

            # Stores return address in R14 (or might get overwritten if no arguments)
            "@5",
            "A=D-A",  # Get to end_frame - 5
            "D=M",
            "@R14",  # return_address
            "M=D",

            # Repositions return value from callee to argument 0's spot
            "@SP",  # Get return value
            "A=M",
            "D=M",
            "@ARG",  # Store return value at *ARG
            "A=M",
            "M=D",

            # Restore Stack Pointer for caller
            "D=A",  # Currently at *ARG
            "@SP",
            "M=D+1",
        ])

        # Restores the segment pointers of the caller
        for segment in ("THAT", "THIS", "ARG", "LCL"):
            self.extend([
                "@R13",  # Calculate stored address = end_frame - i
                "AM=M-1",  # Decrement end frame
                "D=M",  # Restores value to the caller's segment
                f"@{segment}",
                "M=D"
            ])

        # Goto return address stored in R14
        self.extend([
            "@R14", "A=M", "0;JMP"
        ])
