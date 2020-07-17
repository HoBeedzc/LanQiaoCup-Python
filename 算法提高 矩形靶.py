#坐标以按(0,0)为原点计算
def destory(x,y,n,m,l,r):
    for i in range(-l,l+1):
        for j in range(-r,r+1):
            if (i != 0 or j != 0) and 0 <= x+i < n and 0 <= y+j < m:
                target_map[x+i][y+j] = 1 if target_map[x+i][y+j] else 2

n,m,l,r = list(map(int,input().strip().split()))
target_map = []
for i in range(n):
    target_map.append([int(c) for c in input()])
print()
for i in range(n):
    for j in range(m):
        if target_map[i][j] == 1:
            destory(i,j,n,m,l,r)
for i in range(n):
    for j in range(m):
        if target_map[i][j] == 2:
            print(1,end = "")
        else:
            print(target_map[i][j],end = "")
    print()
