# Enter your code here. Read input from STDIN. Print output to STDOUT

def qsort(arr):
    c , r , l = [], [], [];
    if len(arr) <2:
        return arr
    for i in arr:
        if i == arr[0]:
            c.append(i)
        elif i < c[0] :
            l.append(i);
        else:
            r.append(i);
    sub = qsort(l)+c+qsort(r)
    print(' '.join([str(x) for x in sub]))
    return sub

    print(l+c+r)
if __name__ == "__main__":
    n  = int(input());
    arr = list(map(int, input().rstrip().split() ))
    qsort(arr);
