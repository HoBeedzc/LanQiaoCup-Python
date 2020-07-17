def best_road(n,a):
    ans = [[0]]
    for i in range(n):
        temp = []
        for j in range(i+1):
            if j == 0 :
                temp.append(a[i][j]+ans[i][j])
            elif j == i:
                temp.append(a[i][j]+ans[i][j-1])
            else:
                temp.append(a[i][j]+max(ans[i][j],ans[i][j-1]))
        ans.append(temp)
    return max(ans[-1])

n = int(input())
tri = []
for i in range(n):
    tri.append(list(map(lambda x:int(x),input().split())))
print(best_road(n,tri))