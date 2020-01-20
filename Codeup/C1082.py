a = input()

if a == "A":
    r = 10
    for i in range(1,16):
        print("%s*%X=%X"%(a, i, i*r))
elif a == "B":
    r = 11
    for i in range(1,16):
        print("%s*%X=%X"%(a, i, i*r))
elif a == "C":
    r = 12
    for i in range(1,16):
        print("%s*%X=%X"%(a, i, i*r))
elif a == "D":
    r = 13
    for i in range(1,16):
        print("%s*%X=%X"%(a, i, i*r))
elif a == "E":
    r = 14
    for i in range(1,16):
        print("%s*%X=%X"%(a, i, i*r))
else :
    r =15
    for i in range(1,16):
        print("%s*%X=%X"%(a, i, i*r))

