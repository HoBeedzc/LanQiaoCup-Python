n = int(input())
for i in range(10000,1000000):
    a = str(i)
    if a==a[::-1] and sum(list(map(int,list(a))))==n:
        print(i)
