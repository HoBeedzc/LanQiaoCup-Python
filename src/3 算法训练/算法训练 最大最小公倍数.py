n = int(input())
if n%2:
    print(n*(n-1)*(n-2))
else:
    if n%3:
        print(n*(n-1)*(n-3))
    else:
        print((n-1)*(n-2)*(n-3))
