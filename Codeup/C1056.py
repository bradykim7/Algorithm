a,b = input().split(" ")
a = int(a)
b = int(b)

print("%d" %((a and not(b)) or (not(a) and b)) )

