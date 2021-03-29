def is_leap_year(n):
    if n%400==0:
        return 1
    elif n%4==0:
        if n%100==0:
            return 0
        else:
            return 1
    else:
        return 0

year = int(input())
flag = is_leap_year(year)
if flag:
    print('yes')
else:
    print('no')
