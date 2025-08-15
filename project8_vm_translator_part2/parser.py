class Parser:
    arithmetic_commands = ["add", "sub", "neg", "eq", "gt", "lt", "and", "or", "not"]

    def __init__(self, vm_code):

        self.instructions = vm_code
        self.current_index = -1
        self.current_command = None

    def has_next(self):
        return self.current_index < len(self.instructions) - 1

    def advance(self):
        """advances to next command, and updates the current command"""
        self.current_index += 1
        self.current_command = self.instructions[self.current_index].strip()

    def command_type(self):
        c = self.current_command.split()[0].strip().lower()
        if c in self.arithmetic_commands:
            return "C_ARITHMETIC"
        elif c == "push":
            return "C_PUSH"
        elif c == "pop":
            return "C_POP"
        elif c == "label":
            return "C_LABEL"
        elif c == "goto":
            return "C_GOTO"
        elif c == "if-goto":
            return "C_IF"
        elif c == "function":
            return "C_FUNCTION"
        elif c == "call":
            return "C_CALL"
        elif c == "return":
            return "C_RETURN"
        else:
            print(f"UNIDENTIFIED TYPE {self.current_command}")

    def parse_line(self):
        """
        Splits the current line into its components and returns them as appropriate.

        :return command: the command type
        :return arg1: returns first argument of the current command (the command itself for arithmetic, None for return type)
        :return arg2: returns second argument of current command (only for push, pop, function, and call)
        """
        tokens = self.current_command.split()
        tokens = [t.strip() for t in tokens]

        command = tokens[0]
        command_type = self.command_type()

        arg_1 = None
        if command_type != "C_RETURN" and len(tokens) > 1:
            arg_1 = tokens[1]
            # print("Command:", arg_1)
        if command_type == "C_ARITHMETIC":
            arg_1 = command

        arg_2 = None
        if command in ["push", "pop", "function", "call"]:
            arg_2 = tokens[2]

        return command_type, arg_1, arg_2
