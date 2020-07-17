n,m,p = list(map(int,input().split()))
f = [1,1]
for i in range(2,max(n,m)):
    f.append(f[-1]+f[-2])
print(sum(f[:n])%f[m-1]%p)
