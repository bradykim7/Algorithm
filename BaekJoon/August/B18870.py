from sys import stdin

n= int(input())
d =[0]*n
l = list(map(int, input().rsplit()))

temp = set()
for i in l:
    temp.add(i)

temp =sorted(temp)

s = {}
for i in range(len(temp)):
    s[temp[i]] = i

for i in range(len(l)):
    d[i]= s[l[i]]

for i in d:
    print(i, end=" ")