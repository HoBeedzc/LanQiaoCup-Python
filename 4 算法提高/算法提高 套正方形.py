n = int(input())
square = ['**','**']
for i in range(1,(n-2)//2+1):
    if square[0][0] == '*':
        m = ' '
    else:
        m = '*'
    for j in range(len(square)):
        square[j] = m + square[j] + m
    square.insert(0,m*(2*i+2))
    square.append(m*(2*i+2))
for c in square:
    print(c)