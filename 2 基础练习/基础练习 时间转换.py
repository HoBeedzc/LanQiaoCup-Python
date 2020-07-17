t = int(input())
h = t//3600
t = t%3600
m = t//60
t = t%60
print("{}:{}:{}".format(h,m,t))
