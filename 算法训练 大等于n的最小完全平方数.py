import math

n = int(input())
if n<=0:
    print(0)
else:
    sqrt_n = math.sqrt(n)
    if sqrt_n-int(sqrt_n)==0:
        ans = math.pow(sqrt_n,2)
    else:
        ans = math.pow(int(sqrt_n)+1,2)
    print(int(ans))
