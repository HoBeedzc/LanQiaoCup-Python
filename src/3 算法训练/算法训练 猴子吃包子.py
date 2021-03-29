x,y,z,x1,y1,z1,f = map(int,input().split())
print('{:.{n}f}'.format(x1/x+y1/y+z1/z,n = f))
