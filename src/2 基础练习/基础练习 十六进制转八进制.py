#第一种自己写的通过10进制作为中间桥梁，总是超时，wdnmd。
'''
def sixteen2eight(n):
    ten = 0
    for i in range(len(n)):
        c = n[-i-1]
        if c.isalpha():
            c = ord(c)-55
        else:
            c = int(c)
        ten += c*16**i
    l = 0
    i=0
    while(ten):
        l+=ten%8*10**i
        i+=1
        ten = ten//8
    return l

n = int(input())
l = []
for i in range(n):
    num = input()
    l.append(sixteen2eight(num))
for i in range(len(l)):
    print(l[i])
'''
#3位16进制就是4位8进制，（对于二进制来说），所以还是考虑二进制比较方便

#由于python自带进制转换函数，所以这道题实现起来会比较简单
n = int(input())
l = []
for i in range(n):
    l.append(oct(eval('0x'+input()))[2:])#oct()是转换为8进制的函数，‘0x’前缀代表是一个16进制的数字
for i in range(len(l)):
    print(l[i])
