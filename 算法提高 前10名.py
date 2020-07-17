n = input()
l = list(map(int,input().split()))
l.sort(reverse=True)
for c in l[:10]:
    print(c,end = ' ')