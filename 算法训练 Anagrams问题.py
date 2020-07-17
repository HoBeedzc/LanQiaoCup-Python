a = input().lower()
b = input().lower()
a = list(a)
a.sort()
b = list(b)
b.sort()
if a == b:
    print('Y')
else:
    print('N')