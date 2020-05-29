
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the balancedSums function below.
def balancedSums(arr):
    psum = 0
    sum_acc = []
    for x in arr:
        psum += x
        sum_acc.append(psum)

    for i in range(len(arr)):
        if i == 0:
            sum_left = 0
        else:
            sum_left = sum_acc[i-1]

        sum_right = sum_acc[-1] - sum_acc[i]
        if sum_left == sum_right:
            return "YES"

    return "NO"



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    T = int(input().strip())

    for T_itr in range(T):
        n = int(input().strip())

        arr = list(map(int, input().rstrip().split()))

        result = balancedSums(arr)

        fptr.write(result + '\n')

    fptr.close()
