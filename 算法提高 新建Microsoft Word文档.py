n = int(input())
file = [1]
for i in range(n):
    ol = input().split()
    if ol[0]=="New":
        file.append(0)
        location = file.index(0)
        print(location)
        file[location] = 1
    elif ol[0] == "Delete":
        try:
            if(file[int(ol[-1])] == 0):
                print("Failed")
            else:
                file[int(ol[-1])] = 0
                print("Successful")
        except IndexError:
            print("Failed")
