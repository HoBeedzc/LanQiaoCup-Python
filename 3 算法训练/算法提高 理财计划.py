k,n,p = input().split()
mon = int(k)
p = float(p)
for i in range(int(n)):
    mon += mon*p
    mon += int(k)
print("{:.2f}".format(int(100*(mon-int(k)*(int(n)+1)))/100))