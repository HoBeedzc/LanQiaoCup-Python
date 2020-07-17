def cofactor(x,y,n,a):
    ans = []
    for i in range(n):
        if i-x:
            temp = []
            for j in range(n):
                if j-y:
                    temp.append(a[i][j])
            ans.append(temp)
    return ans

def delta(n,a):
    if n == 2:
        return a[0][0]*a[1][1]-a[0][1]*a[1][0]
    elif n == 1:
        return a[0][0]
    else:
        SUM = 0
        for i in range(n):
            SUM += (-1)**i*a[0][i]*delta(n-1,cofactor(0,i,n,a))
        return SUM

n = int(input())
a = []
for i in range(n):
    a.append(list(map(lambda x:int(x),input().split())))
print(delta(n,a))
