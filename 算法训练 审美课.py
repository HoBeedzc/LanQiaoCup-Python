n,m = list(map(int,input().split()))
count = 0;
all_judge = []
for i in range(n):
    judge = eval("0b"+input().replace(" ",""))
    all_judge.append(judge)
    for c in all_judge:
        if c^judge == 2**m-1:
            count += 1
print(count)
