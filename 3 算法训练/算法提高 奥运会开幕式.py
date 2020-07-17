def get_out(a,m):
    for i in range(m-1):
        a.append(a.pop(0))
    return a.pop(0)

n,m = list(map(lambda x:int(x),input().split()))
a = [i+1 for i in range(n)]
angle = 0
while(a):
    angle = get_out(a,m)
print(angle)
