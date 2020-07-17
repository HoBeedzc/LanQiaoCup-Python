def gpa():
    n = int(input())
    if n==0:
        return 0
    s = 0
    c = 0
    for i in range(n):
        try:
            si,ci = list(map(int,input().split()))
        except:
            continue
        c += si*ci
        s += si
    return c/s

if __name__=="__main__":
    a = gpa()
    b = gpa()
    c = abs(a-b)
    if 0<=c<= 0.05:
        print("{:.2f}".format(0))
    elif a<b:
        print("-{:.2f}".format(c))
    elif a>b:
        print("{:.2f}".format(c))
