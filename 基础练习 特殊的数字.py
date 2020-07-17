for i in range(100,1000):
    a = int(str(i)[0])
    b = int(str(i)[1])
    c = int(str(i)[2])
    if i == a**3+b**3+c**3:
        print(i)
