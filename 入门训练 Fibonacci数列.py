n = int(input());
F = [1,1]
for i in range(2,n):
	F.append((F[i-2]+F[i-1])%10007)
print(F[-1])
