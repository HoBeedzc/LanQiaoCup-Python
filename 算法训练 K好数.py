k, l = map(int, input().split())
ans = [0] + [1 for i in range(k - 1)]
ans_1 = [0] + [1 for i in range(k - 1)]
for i in range(l - 1):
    for j in range(k):
        if j == 0:
            ans_1[j] = sum(ans[2:]) + ans[0]
        elif j == k - 1:
            ans_1[j] = sum(ans[:-2]) + ans[-1]
        else:
            ans_1[j] = sum(ans[:j - 1] + ans[j + 2:]) + ans[j]
    for j in range(k):
        ans[j] = ans_1[j]
if l == 1:
    if k == 1:
        print(0)
    else:
        print((sum(ans) + 1) % 1000000007)
else:
    print(sum(ans) % 1000000007)
