def partition(start, end):
    global arr
    if end - start > 0:
        pivot, border = arr[end], start
        for i in range(start, end):
            if arr[i] < pivot:
                arr[i], arr[border] = arr[border], arr[i]
                border +=1
        arr[end], arr[border] = arr[border], arr[end]
        print(' '.join([str(x) for x in arr]))
        partition(start, border-1) #Sort Left
        partition(border+1, end) #Sort Right


m = int(input().strip())
arr = list(map(int, input().strip().split()))
partition(0, m-1)