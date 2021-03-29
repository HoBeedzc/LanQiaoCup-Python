n = int(input())
if n == 1:
    print(2)
else:
    zhishu = [2]
    cur = 3
    cnt = 1
    while True:
        flag = 1
        for i in zhishu:
            if cur % i == 0:
                flag = 0
        if flag:
            zhishu.append(cur)
            cnt += 1
        cur += 1
        if cnt == n:
            break
    ans = 1
    for c in zhishu:
        ans *= c
        ans %= 50000
    print(ans)
