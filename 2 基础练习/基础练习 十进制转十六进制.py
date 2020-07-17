#无脑函数法(这个只得了81分...)
'''
print(str(hex(int(input())))[2:].upper())
'''
#还是自己写来的实在...(之前没有考虑0的情况，我太弟弟了)
def ten2sixteen(ten):
    l = ''
    turn = ['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F']
    while(1):
        l+=turn[ten%16]
        ten = ten//16
        if not ten:
            return l[::-1]

print(ten2sixteen(int(input())))
