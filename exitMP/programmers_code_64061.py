def solution(board, moves):
    answer = []
    result = 0
    l = []
    n = len(board)
    for y in range(n):
        line = []
        for x in range(n):
            if board[x][y] == 0:
                continue
            else:
                line.append(board[x][y])
        l.append(line)
    for i in moves:
        while True:
            if len(l[i-1]) != 0:
                target = l[i-1].pop(0)
                answer.append(target)
                if len(answer) >= 2 and answer[-1] == answer[-2]:
                    answer.pop()
                    answer.pop()
                    result += 2
                break
            else:
                break
    return result


kk = solution([[0, 0, 0, 0, 0], [0, 0, 1, 0, 3], [0, 2, 5, 0, 1], [
               4, 2, 4, 4, 2], [3, 5, 1, 3, 1]], [1, 5, 3, 5, 1, 2, 1, 4])
print(kk)