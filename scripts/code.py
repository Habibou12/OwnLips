class Code:
    def __init__(self):
        # Tables de traduction pour le Hack Assembler

        # Table COMP (Retourne les 7 bits : a c1 c2 c3 c4 c5 c6)
        self.comp_table = {
            # Quand a == 0
            "0": "0101010", "1": "0111111", "-1": "0111010",
            "D": "0001100", "A": "0110000", "!D": "0001101",
            "!A": "0110001", "-D": "0001111", "-A": "0110011",
            "D+1": "0011111", "A+1": "0110111", "D-1": "0001110",
            "A-1": "0110010", "D+A": "0000010", "D-A": "0010011",
            "A-D": "0000111", "D&A": "0000000", "D|A": "0010101",

            # Quand a == 1
            "M": "1110000", "!M": "1110001", "-M": "1110011",
            "M+1": "1110111", "M-1": "1110010", "D+M": "1000010",
            "D-M": "1010011", "M-D": "1000111", "D&M": "1000000",
            "D|M": "1010101"
        }

        # Table DEST (Retourne les 3 bits : d1 d2 d3)
        self.dest_table = {
            "": "000", "M": "001", "D": "010", "MD": "011",
            "A": "100", "AM": "101", "AD": "110", "ADM": "111"
        }

        # Table JUMP (Retourne les 3 bits : j1 j2 j3)
        self.jump_table = {
            "": "000", "JGT": "001", "JEQ": "010", "JGE": "011",
            "JLT": "100", "JNE": "101", "JLE": "110", "JMP": "111"
        }
    def dest(self, string):
        return self.dest_table[string]
    def compt(self, stirng):
        return self.comp_table[stirng]
    def jump(self, string):
        return self.jump_table[string]
