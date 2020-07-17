#MLE TLE
def oper1(l,r,d):
    for i in range(l-1,r):
        num[i] += d
    return 0

def oper2(l1,r1,l2,r2):
    if l1 > l2:
        step = l1-l2
        for i in range(l1-1,r1,-1):
            num[i] = num[i-step]
    elif l1 < l2:
        step = l2-l1
        for i in range(l1-1,r1):
            num[i] = num[i+step]
    else:
        pass

def oper3(l,r):
    return sum(num[l-1:r])

if __name__=="__main__":
    Case = int(input())
    n,m = list(map(int,input().split()))
    num = list(map(int,input().split()))
    for i in range(m):
        temp = list(map(int,input().split()))
        if temp[0] == 1:
            oper1(temp[1],temp[2],temp[3])
        elif temp[0] == 2:
            oper2(temp[1],temp[2],temp[3],temp[4])
        else:
            print(oper3(temp[1],temp[2]))