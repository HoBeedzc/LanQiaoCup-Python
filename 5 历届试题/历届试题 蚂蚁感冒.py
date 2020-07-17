n = int(input())
ants = list(map(int,input().split()))
count = 1
patient = ants[0]
if patient > 0:#->
    for c in ants:
        if abs(c) > abs(patient) and c*patient < 0:
                count += 1
    if count != 1:
        for c in ants:
            if abs(c) < abs(patient) and c*patient > 0:
                count += 1
else:
    for c in ants:
        if abs(c) < abs(patient) and c*patient < 0:
                count += 1
    if count != 1:
        for c in ants:
            if abs(c) > abs(patient) and c*patient > 0:
                count += 1
print(count)