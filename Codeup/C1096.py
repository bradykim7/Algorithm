a = int(input())
b = [[0]*19 for i in range(19)]

for i in range(a):
    x,y=map(int,input().split(" "))
    b[x-1][y-1] +=1

for j in range(19):
    for k in range(19):
        print(b[j][k], end=" ")
    print()

