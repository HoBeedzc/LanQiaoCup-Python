n = int(input())
num = list(map(int,input().split()))
m = int(input())
ans = []
for i in range(m):
    l,r,k = list(map(int,input().split()))
    temp = num[l-1:r]
    temp.sort()
    ans.append(temp[-k])
for c in ans:
    print(c)
