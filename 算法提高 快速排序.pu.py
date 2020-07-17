def quick_sort(a):
    b = []
    c = []
    std = a[0]
    for item in a:
        if item < std:
            b.append(item)
            #print("b = ",b)
        else:
            c.append(item)
            #print("c = ",c)
    c.pop(0)
    if len(b) > 1:
        a_1 = quick_sort(b)
    else:
        a_1 = b
    if len(c) > 1:
        a_2 = quick_sort(c)
    else:
        a_2 = c
    a_1.append(a[0])
    return a_1 + a_2

a = quick_sort(list(map(lambda x:int(x),input().split()[:-1])))
for c in a:
    print(c,end=" ")
