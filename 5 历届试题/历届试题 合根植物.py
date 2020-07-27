m, n = map(int, input().split())
matrix = [[] for i in range(m * n)]
step = int(input())
for i in range(step):
    a, b = map(int, input().split())
    matrix[a - 1].append(b - 1)
    matrix[b - 1].append(a - 1)
cnt = 0
ans = [0 for i in range(n * m)]
for i in range(m * n):
    if ans[i] != 0:
        pass
    else:
        k = i
        cnt += 1
        ans[k] = cnt
        stack = [k]
        while stack != []:
            flag = 1
            for j in matrix[k]:
                if ans[j] != 0:
                    pass
                else:
                    ans[j] = cnt
                    stack.append(k)
                    k = j
                    flag = 0
                    break
            if flag:
                k = stack.pop(-1)
print(cnt)
'''
for i in range(m):
    for j in range(n):
        print(ans[i*n + j],end=' ')
    print()
'''
