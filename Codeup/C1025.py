a=input()
length = len(a)-1

for i in str(a):
    print("[%d]" %(int(i)*10**length))
    length-=1

