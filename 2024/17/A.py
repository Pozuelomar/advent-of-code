a = 37283687
b = 0
c = 0
program = [2, 4, 1, 3, 7, 5, 4, 1, 1, 3, 0, 3, 5, 5, 3, 0]
pointer = 0


def getcombo(i):
    if i <= 3:
        return i
    if i == 4:
        return a
    if i == 5:
        return b
    if i == 6:
        return c
    if i == 7:
        raise Exception("Invalid combo 7")


while 0 <= pointer < len(program):
    instr = program[pointer]
    literal = program[pointer + 1]
    combo = getcombo(literal)
    if instr == 0:
        a >>= combo
    elif instr == 1:
        b ^= literal
    elif instr == 2:
        b = combo % 8
    elif instr == 3:
        if a != 0:
            pointer = literal
            continue
    elif instr == 4:
        b ^= c
    elif instr == 5:
        print(combo % 8, ",", sep="", end="")
    elif instr == 6:
        b = a >> combo
    elif instr == 7:
        c = a >> combo
    pointer += 2

print()
