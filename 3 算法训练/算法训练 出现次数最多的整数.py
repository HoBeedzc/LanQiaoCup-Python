n  = int(input())
try:
    prenum = 0
    nownum  = 0
    num_count = []
    all_num = []
    count = 0
    for i in range(n):
        nownum = int(input())
        if nownum != prenum :
            all_num.append(nownum)
            num_count.append(count)
            count = 1
        else:
            count += 1
        prenum = nownum
    num_count.append(count)
    num_count.pop(0)
    print(all_num[num_count.index(max(num_count))])
except:
    pass
