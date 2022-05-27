def solution(N, stages):
    answer = {x: 0 for x in range(1, N+1)}
    l = {x: 0 for x in range(1, N+1)}
    total = len(stages)
    stages.sort()
    for i in stages:
        if i > N:
            continue
        l[i] += 1

    for x, y in l.items():
        if total <= 0:
            answer[x] = 0
        else:
            answer[x] = y / total
            total -= l[x]


    print(answer)
    answer = sorted(answer, key=answer.get, reverse=True)
    return answer


kms = solution(5, [1,1,1,2,2,2,2,2,3])

print(kms)
