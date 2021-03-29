n,m = map(int,input().split())
l = input().split()
for i in range(m):
    a,b = map(int,input().split())
    l[a-1],l[b-1] = l[b-1],l[a-1]
for c in l:
    print(c)