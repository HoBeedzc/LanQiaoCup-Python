def check(a,b):
    if len(a) != len(b):
        return 1
    else:
        if a == b:
            return 2
        elif a.lower() == b.lower():
            return 3
        else:
            return 4
            
a = input()
b = input()
print(check(a,b))
