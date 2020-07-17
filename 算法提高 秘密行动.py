def dp(height):
    climb.append(min(jump[-1],climb[-1])+height)
    jump.append(min(climb[-2],climb[-3]))
n = int(input())
jump = [0]
climb = [0,0]
for i in range(n):
    dp(int(input()))
print(min(jump[-1],climb[-1]))