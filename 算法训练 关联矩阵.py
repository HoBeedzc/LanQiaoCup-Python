n, m = map(int, input().split())
ans = [[' 0' for i in range(m)] for j in range(n)]
for i in range(m):
    a, b = map(int, input().split())
    ans[a - 1][i] = ' 1'
    ans[b - 1][i] = '-1'
for i in ans:
    print(*i)