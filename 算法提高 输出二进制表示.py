n = int(input())
for i in range(8):
    print((n>>7-i)&1,end = '')
print()