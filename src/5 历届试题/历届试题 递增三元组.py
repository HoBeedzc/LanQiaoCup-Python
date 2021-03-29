def f(item,ii,ji):
    for i in range(n-1,ii-1,-1):
        for j in range(ji,n):
            if a[i] < item < c[j]:
                return (i+1)*(n-j),i,j
    return 0,ii,ji

n = int(input())
a = list(map(int,input().split()))
b = list(map(int,input().split()))
c = list(map(int,input().split()))
a.sort()
b.sort()
c.sort()
count = 0
ii = 0
ji = 0
for item in b:
    temp,ii,ji = f(item,ii,ji)
    count += temp
print(count)