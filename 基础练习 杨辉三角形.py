n = int(input())
yanghui = [[1],[1,1]]
for i in range(3,n+1):
    line = [1]
    for j in range(i-2):
        line.append(yanghui[-1][j]+yanghui[-1][j+1])
    line.append(1)
    yanghui.append(line)
for c in yanghui:
    print(' '.join(list(map(str,c))))
