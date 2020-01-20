w, h= map(int, input().split(" "))
matrix = [[0]*h for i in range(w)]

n= int(input())

for i in range(n):
    l,d,x,y = map(int, input().split(" "))
    
    if d ==0:
        for j in range(l):
            matrix[x-1][y-1+j] =1
    else:
        for k in range(l):
            matrix[x-1+k][y-1] =1

for m in range(w):
    for n in range(h):
        print(matrix[m][n],end=" ")
    print()



