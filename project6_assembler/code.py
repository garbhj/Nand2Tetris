class Code:
    comp_codes = {
        '0': '0101010', '1': '0111111', '-1': '0111010',
        'D': '0001100', 'A': '0110000', '!D': '0001101',
        '!A': '0110001', '-D': '0001111', '-A': '0110011',
        'D+1': '0011111', 'A+1': '0110111', 'D-1': '0001110',
        'A-1': '0110010', 'D+A': '0000010', 'D-A': '0010011',
        'A-D': '0000111', 'D&A': '0000000', 'D|A': '0010101',
        'M': '1110000', '!M': '1110001', '-M': '1110011',
        'M+1': '1110111', 'M-1': '1110010', 'D+M': '1000010',
        'D-M': '1010011', 'M-D': '1000111', 'D&M': '1000000',
        'D|M': '1010101'
    }
    dest_codes = {
        "": "000",
        "M": "001",
        "D": "010",
        "MD": "011",
        "A": "100",
        "AM": "101",
        "AD": "110",
        "AMD": "111"
    }
    jump_codes = {
        "": "000",
        "JLT": "100",
        "JEQ": "010",
        "JGT": "001",
        "JLE": "110",
        "JGE": "011",
        "JNE": "101",
        "JMP": "111"
    }

    def a_encode(self, address):
        return "0" + f"{self.binary_encode(address):0>15}"

    def c_encode(self, comp, dest, jump):
        comp = self.comp_codes[comp]
        dest = self.dest_codes[dest]
        jump = self.jump_codes[jump]
        return "111" + comp + dest + jump

    def binary_encode(self, num):
        return bin(int(num))[2:]  # 14 least significant bits
