L,R = list(map(int,input().split()))
count = 0
for i in range(L,R+1):
    count += bin(i)[2:].count("1")
print(count)
