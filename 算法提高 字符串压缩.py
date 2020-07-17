def compress(n):
    dic = {}
    ans = ''
    for i in n:
        count = dic.get(i,0) + 1
        if (count in [1,3,6]) or (i == ' '):
            ans += i
        dic[i] = count
    return ans

print(compress(input()))