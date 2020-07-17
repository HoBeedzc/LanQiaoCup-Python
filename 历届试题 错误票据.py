n = int(input())
l = []
for i in range(n):
    l.extend(list(map(int,input().split())))
l.sort()
a = 0
b = 0
for c in range(len(l)-1):
    if l[c] + 1 == l[c+1]:
        pass
    elif l[c] + 2 == l[c+1]:
        a = l[c] + 1
        if b:
            break
    else:
        b = l[c]
        if a:
            break
print("{} {}".format(a,b))