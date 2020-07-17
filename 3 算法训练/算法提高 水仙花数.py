for i in range(100,1000):
    a = str(i)
    b = int(a[0])
    c = int(a[1])
    d = int(a[2])
    if b**3+c**3+d**3 == i:
        print(i)
