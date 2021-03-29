n,k,t = list(map(int,input().split()))
sum = 1
for i in range(1,t):
    sum += ((1+n*i)*(n*i)//2+1)%k
print(sum)