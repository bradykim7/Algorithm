def solution(n, arr1, arr2):
    answer = []

    for i in range(n) : 
        c = format(n, bin(arr1[i]))
        a = "{0:b}".format(arr1[i])
        b = "{0:b}".format(arr2[i])
        print(a,b)
        print(c)
        
    return answer


kms = solution(5, [9, 20, 28, 18, 11], [30, 1, 21, 17, 28])