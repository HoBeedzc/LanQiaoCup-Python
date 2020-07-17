#二进制思想
for i in range(32):
    ans = str(bin(i))[2:]
    if len(ans)!=5:
        ans = '0'*(5-len(ans))+ans
    print(ans)
