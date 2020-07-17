def f(m,n):
    if m < n:
        return 0
    elif n == 0:
        return 1
    else:
        return f(m - 1, n) + f(m,n - 1)

if __name__=='__main__':
    m,n = map(int,input().split())
    print(f(m,n))
