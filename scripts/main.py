from parserhack import *
from code import *
from SymbTable import *

parser = Parser()
code  = Code()
symbtable = SymbTable()


f = open('Binaire.txt', 'w')

def firstPass():
    while parser.hasMoreLine():
        parser.advance()
        if parser.type == 'L':
            symbol = parser.symbol
            symbtable.addsymbol(symbol, parser.currentLineIndex-1)
    parser.currentLineIndex = 0

def secondPass():
    while parser.hasMoreLine():

        parser.advance()
        currentline = ""

        if parser.type == 'A':

            symbol = parser.symbol

            if symbol.isnumeric():
                currentline += f"{int(symbol):016b}"
            elif symbtable.symbol.get(symbol) is not None:
                print(symbol)
                value = symbtable.symbol[symbol]

                currentline += f"{int(value):016b}"
            else:

                value = symbtable.addsymbol(symbol, symbtable.start)
                symbtable.start += 1
                currentline += f"{int(value):016b}"


        elif parser.type == 'C':
            currentline = "111"
            dest = parser.dest
            comp = parser.comp
            jump = parser.jump
            currentline += code.compt(comp)
            currentline += code.dest(dest)
            currentline += code.jump(jump)
        else:
            continue


        f.write(currentline + '\n')
firstPass()
secondPass()
f.close()












