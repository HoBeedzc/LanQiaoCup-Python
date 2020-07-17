#第一种无脑函数法
'''
print(int(eval('0x'+input())))
'''
#第二种要自己写进制转换的算法(这个也A了...)
def sixteen2ten(n):
    ten = 0
    for i in range(len(n)):
        c = n[-i-1]
        if c.isalpha():
            c = ord(c)-55
        else:
            c = int(c)
        ten += c*16**i
    return ten

print(sixteen2ten(input()))
