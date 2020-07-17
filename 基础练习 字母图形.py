n,m = list(map(int,input().split()))
l = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
l_r = l[::-1]
print(l[:m])
for i in range(1,n):
    if i>=26:
        i -= 26
    print(l_r[-i-1:]+l[1:m-i])
