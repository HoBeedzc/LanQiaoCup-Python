n,Q = list(map(int,input().split()))
l = list(map(int,input().split()))
for i in range(Q):
    lo,hi = list(map(int,input().split()))
    hi += 1
    print(min(l[lo:hi]))
