n = input()
num = list(map(int,input().split()))
a = int(input())
try:
    print(num.index(a)+1)
except:
    print(-1)
