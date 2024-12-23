# [2, 4, 1, 3, 7, 5, 4, 1, 1, 3, 0, 3, 5, 5, 3, 0]
# b = a % 8
# b = b ^ 3
# c = a >> b
# b = b ^ c
# b = b ^ 3
# a = a >> 3
# print(b % 8)
# if a>0 goto 0


# b1 is next 3 bits of a [%8]
# c is a >> (b1 xor 3)   [%8]
# b3 is b1 xor c         [%8]
# print b3               [%8]


# find the smallest b1 ins range(8) that satisfies:
# b1 ^ c == program[-1]:
#  where
#  c = (newa >> (b1 ^ 3)) % 8
#  with newa = (a << 3) | b1

# if failed to find, backtrack


def foo(a, program):
    if not program:
        return a
    b3 = program.pop()
    for b1 in range(8):
        if a == 0 and b1 == 0:
            continue
        newa = (a << 3) | b1
        c = (newa >> (b1 ^ 3)) % 8
        if b1 ^ c == b3:
            if x := foo(newa, program):
                return x
    else:
        program.append(b3)
        return


a = foo(0, [2, 4, 1, 3, 7, 5, 4, 1, 1, 3, 0, 3, 5, 5, 3, 0])
print(a)


def compute(a):

    b = 0
    c = 0
    program = [2, 4, 1, 3, 7, 5, 4, 1, 1, 3, 0, 3, 5, 5, 3, 0]
    pointer = 0

    output = []

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
            output.append(combo % 8)
        elif instr == 6:
            b = a >> combo
        elif instr == 7:
            c = a >> combo
        pointer += 2
    return output


print(compute(a))
