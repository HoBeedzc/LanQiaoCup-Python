n,m = map(int,input().split())
l = list(map(int,input().split()))
max_sum = 0
for i in range(n):
    temp = sum(l[:m])
    max_sum = temp if temp > max_sum else max_sum
    l.append(l.pop(0))
print(max_sum)