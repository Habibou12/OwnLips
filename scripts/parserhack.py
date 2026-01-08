class Parser:
    def __init__(self):
        f = open('hack.asm', 'r')
        contenu = f.read().splitlines()
        f.close()
        self.contenu = contenu
        self.totalLine = len(contenu)
        self.currentLineIndex= 0
        self.currentLine = None
        self.type = None
        self.symbol = None
        self.dest = None
        self.comp = None
        self.jump = None

    def hasMoreLine(self):
        return self.currentLineIndex != self.totalLine
    def advance(self):

        self.currentLine = self.contenu[self.currentLineIndex]
        self.currentLine = self.currentLine.strip()

        self.currentLineIndex += 1

        if self.currentLine[0] == '@':

            self.type = 'A'
            self.symbol = self.currentLine[1:]
        elif self.currentLine[0] == '(':
            self.type = 'L'
            self.symbol = self.currentLine[1:-1]
        elif self.currentLine[0] == '/':
            self.type = 'T'

        else:
            self.type = 'C'
            index = 0

            while index < len(self.currentLine) and self.currentLine[index] != '=':
                index += 1
            if index == len(self.currentLine):
                index = 0
                start = index-1
            else:
                start = index
            self.dest = self.currentLine[:index]
            while index < len(self.currentLine) and self.currentLine[index] != ';' :
                index += 1
            self.comp = self.currentLine[start+1:index]

            self.jump = self.currentLine[index+1:]
