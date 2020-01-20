a= int(input())
b= map(int, input().split(" "))
result = 9999

for i in b:
    if result > i:
        result =i
print(result)

