def solution(n, arr1, arr2):
    answer = []
    for i in range(n):
        f = "{0:0"+str(n)+"b}"
        tmp = f.format(arr1[i] | arr2[i])
        tmp = tmp.replace("1", "#")
        tmp = tmp.replace("0", " ")
        answer.append(tmp)
    return answer


kms = solution(5, [9, 20, 28, 18, 11], [30, 1, 21, 17, 28])

