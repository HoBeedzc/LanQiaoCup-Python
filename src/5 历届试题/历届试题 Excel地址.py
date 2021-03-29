def turn(n):
    l = []
    while(n):
        c = n%26
        if c == 0:
            c = 26
        l.append(chr(c+64))
        if c == 26:
            n = n//26-1
        else:
            n = n//26
    return "".join(l[::-1])

n = int(input())
print(turn(n))