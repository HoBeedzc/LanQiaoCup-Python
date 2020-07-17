n = int(input())
AS,BS = 0,0
for i in range(n):
    a,b = map(int,input().split())
    AS += a
    BS += b
print("{}+{}i".format(AS,BS))