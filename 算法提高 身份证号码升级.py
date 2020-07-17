def update(old):
    new = old[:6] + '19' +old[6:]
    power = [7,9,10,5,8,4,2,1,6,3,7,9,10,5,8,4,2]
    sum = 0
    for i in range(len(new)):
        sum += int(new[i])*power[i]
    new += "10x98765432"[sum%11]
    return new

if __name__=="__main__":
    print(update(input()))