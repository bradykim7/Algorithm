#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the getMinimumCost function below.
def getMinimumCost(k, c):
    c = sorted(c)
    ans = 0
    if k == len(c):
        for i in c:
            ans += i
        return ans

    i = len(c)
    index = 0
    count = 0
    while i > 0:
        # print((1+index)*c[i-1])
        ans += (1 + index) * c[i - 1]
        i -= 1
        count += 1

        if count == k:
            index += 1
            count = 0
    return (ans)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    c = list(map(int, input().rstrip().split()))

    minimumCost = getMinimumCost(k, c)

    fptr.write(str(minimumCost) + '\n')

    fptr.close()
