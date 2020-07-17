def Maximum_product():
    n,m = list(map(int,input().split()))
    l = list(map(int,input().split()))
    l.sort()
    if m%2:
        total = [l.pop(-1)]
    else:
        total = [1]
    for i in range(m//2):
        if l[-1]*l[-2] >= l[0]*l[1]:
             c = total[-1]*l.pop(-1)*l.pop(-1)
        else:
            c = total[-1]*l.pop(0)*l.pop(0)
        total.append(c)
    print(total[-1])
    return 0

n = int(input())
for i in range(n):
    Maximum_product()
