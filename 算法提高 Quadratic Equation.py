a,b,c = map(float,input().split())
delta = b**2-4*a*c
x1 = (-b+delta**0.5)/(2*a)
x2 = (-b-delta**0.5)/(2*a)
print("{:.2f} {:.2f}".format(max(x1,x2),min(x1,x2)))