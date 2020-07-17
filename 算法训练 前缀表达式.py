a = input().split()
if a[0] == '/':
    print(int(a[1])//int(a[2]))
else:
    print(eval(a[1]+a[0]+a[2]))