def pk(a,b):
    if a == 0:
        if b == 0:
            return 0
        elif b == 1:
            return -1
        else:
            return 1
    elif a == 1:
        if b == 0:
            return 1
        elif b == 1:
            return 0
        else:
            return -1
    else:
        if b == 0:
            return -1
        elif b == 1:
            return 1
        else:
            return 0

a,b = map(int,input().split())
print(pk(a,b))