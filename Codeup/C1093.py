a =int(input())
b= input().split(" ")
c=[]

for i in range(23):
    c.append(0)
    
for i in b:
    c[int(i)-1] +=1
    
for i in c:
    print(i, end=" ")



