n = int(input())
flag = True
for i in range(10000,1000000):
    cuv = str(i)
    if cuv == cuv[::-1]:
        sum = 0
        for j in cuv:
            sum += int(j)
        if sum == n:
            print(i)
            flag = False
    else:
        pass
if flag:
    print(-1)