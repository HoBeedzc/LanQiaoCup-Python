n = input()
m = input().replace("0"," ").split()
print(len(m))
for c in m:
    print(int(c),end = " ")
