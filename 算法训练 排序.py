l = list(map(int,input().split()))
l.sort(reverse=True)
for c in l:
    print(c,end = " ")