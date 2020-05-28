# Enter your code here. Read input from STDIN. Print output to STDOUT
def partition (arr, start, end):
    global ansq
    pivot = arr[end]
    point = start -1

    for i in range(start,end):
        if arr[i] <= pivot :
            ansq+=1
            point+=1
            # Swapping
            arr[i], arr[point] = arr[point], arr[i]
    # Swapping point, thus, pivot's proper place
    arr[point+1], arr[end]= arr[end], arr[point+1]
    ansq+=1
    return point+1

def quicksort(arr,start,end):
    global ansq
    if start < end:
        point = partition(arr,start,end)
        left= quicksort(arr,start,point-1)
        right = quicksort(arr,point+1,end)

    return ansq

def insertsort(arr):
    ans=0
    for i in range(1,len(arr)):
        key = arr[i]
        j =i-1;
        while j >=0 and arr[j] > key:
            arr[j+1] = arr[j]
            j-=1;
            ans+=1
        arr[j+1] = key

    return ans



if __name__ == "__main__":
    n = int(input().rstrip())
    arr1= list(map(int,input().rstrip().split()))
    arr2 = list(arr1)
    ansq =0

    print(insertsort(arr2) - quicksort(arr1,0,n-1))
