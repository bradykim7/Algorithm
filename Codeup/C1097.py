b = []

for i in range(19):
    b.append(input().split(" "))


a = int(input())

for j in range(a):
    x,y = map(int, input().split(" "))
    for k in range(19):
        if b[x-1][k] =="0":
            b[x-1][k] ="1"
        else :
            b[x-1][k] ="0"
            
        if b[k][y-1] =="0":
            b[k][y-1] =1
        else:
            b[k][y-1] ="0"

for i in range(19):
    for j in range(19):
        print(b[i][j], end=" ")
    print(" ")
    


