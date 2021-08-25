arr = []
n = [1, 2, 3, 4, 5, 6, 7, 8, 9]
for i in range(9):
    arr.append(list(map(int, input().rstrip().split())))

for i in range(9):
    print(arr[i][0], end=" ")


# check Row
def cR(num, row):
    if num in arr[row]:
        return False
    else:
        return True


# check Column
def cC(num, col):
    c = []
    for i in range(9):
        c.append(arr[i][col])
    if num in c:
        return False
    else:
        return True


# check Box
def cB(num, row, col):
    for i in range(row // 3, row // 3 + 3):
        for j in range(col // 3, col // 3 + 3):
            if arr[i][j] == num:
                return False
    return True


def f():
    pass
