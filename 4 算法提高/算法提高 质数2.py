# 筛法
n = int(input())
ans = [0] + [1 for i in range(n - 1)]
for i in range(n - 1):
    if ans[i] == 0:
        pass
    else:
        temp = 2 * i + 2
        while temp <= n:
            ans[temp - 1] = 0
            temp += i + 1
cnt = 0
l = []
for i in range(n - 1):
    if ans[i]:
        l.append(i + 1)
        cnt += 1
print(cnt)
print(*l)
