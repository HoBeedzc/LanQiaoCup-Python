def gcd(a,b):
    while(True):
        if(a%b):
            d = a%b
            a = b
            b = d
        else:
            return b

def lcm(a,b):
    return a*b/gcd(a,b)

if __name__ == "__main__":
    a,b,c = list(map(int,input().strip().split()))
    print(int(lcm(lcm(a,b),c)))