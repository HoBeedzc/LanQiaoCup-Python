def calculate(a):
    ans = 0.7*a[0]+0.2*a[1]+0.1*a[2]+a[3]
    return ans if ans < 100 else 100

n = int(input())
for i in range(n):
    print("{:.1f}".format(calculate(list(map(lambda x:int(x),input().split())))))
