import sys 
l = [line.strip() for line in sys.stdin]

def get(i,j):
    if i<0 or i>=len(l) or j<0 or j>=len(l[i]):
        return '.'
    return l[i][j]

def is_part_number(i, j1, j2):
    print(i,j1,j2)
    for a in range(i-1,i+2):
        for b in range(j1-1, j2+2):
            print(a,b)
            if not get(a,b).isnumeric() and get(a,b)!='.':
                return True
    return False

v = 0
length = 0
sum = 0
for i in range(len(l)):
    for j in range(len(l[i])+1):
        if get(i,j).isnumeric():
            length += 1
            v = v*10+int(get(i,j))
            continue
        if length>0:
            if is_part_number(i, j-length, j-1):
                sum +=v
            v = 0
            length = 0
            continue

print(sum)
# 530495