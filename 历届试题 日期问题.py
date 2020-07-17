def year(y):
    if y%4 == 0:
        if y%100 == 0:
            if y%400 == 0:
                return 1
            else:
                return 0
        else:
            return 1
    else:
        return 0

def check(y,m,d):
    if m == '00' or d == '00':
        return -1
    if int(m)>12:
        return -1
    elif int(m) in [1,3,5,7,8,10,12]:
        if int(d) > 31:
            return -1
        if int(y) >= 60:
            l.append('19'+y+'-'+m+'-'+d)
        else:
            l.append('20'+y+'-'+m+'-'+d)
    elif int(m) in [4,6,9,11]:
        if int(d) > 30:
            return -1
        if int(y) >= 60:
            l.append('19'+y+'-'+m+'-'+d)
        else:
            l.append('20'+y+'-'+m+'-'+d)
    else:
        if int(y) >= 60:
            if year(int('19'+y)) and int(d)<=29:
                l.append('19'+y+'-'+m+'-'+d)
            elif not year(int('19'+y)) and int(d)<=28:
                l.append('19'+y+'-'+m+'-'+d)
            else:
                return 0
        else:
            if year(int('20'+y)) and int(d)<=29:
                l.append('20'+y+'-'+m+'-'+d)
            elif not year(int('20'+y)) and int(d)<=28:
                l.append('20'+y+'-'+m+'-'+d)
            else:
                return 0
    return 0

a,b,c = list(input().split('/'))
l = []
check(a,b,c)
check(c,a,b)
check(c,b,a)
l = list(set(l))
l.sort()
for c in l:
    print(c)