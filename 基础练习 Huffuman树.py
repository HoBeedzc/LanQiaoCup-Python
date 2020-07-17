n = int(input())
huffuman = list(map(int,input().split()))
fee = 0
for i in range(n-1):
    temp = huffuman.pop(huffuman.index(min(huffuman)))  + huffuman.pop(huffuman.index(min(huffuman)))
    huffuman.append(temp)
    fee += temp
print(fee)
