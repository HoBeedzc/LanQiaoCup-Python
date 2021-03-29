def gcd(n,m):
    temp = min(n,m)
    while(1):
        if n%temp == 0 and m%temp == 0:
            return temp
        else:
            temp -= 1

n,m = list(map(int,input().split()))
print(int(n*m/gcd(n,m)))
