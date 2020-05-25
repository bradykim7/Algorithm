def insertion_sort(l):
    # Loop invariant Algo
    for i in range(1, len(l)):
        j = i-1
        key = l[i]
        while (j > 0) and (l[j] > key): # l[] == 4
           l[j+1] = l[j]
           j -= 1
        l[j+1] = key

    for i in range(len(l)):
        temp = l[i]
        if i != len(l)-1 and l[i]>l[i+1]:
            l[i]=l[i+1];
            l[i+1]=temp;


m = int(input().strip())
ar = [int(i) for i in input().strip().split()]
insertion_sort(ar)
print(" ".join(map(str,ar)))