#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumDistances function below.
def minimumDistances(a):
    ans =[]
    for i in range(len(a)):
        for j in range(len(a)):
            if a[i] == a[j] and i != j:
                ans.append(abs(j-i));

    if not ans:
        return -1;
    return min(ans)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    a = list(map(int, input().rstrip().split()))

    result = minimumDistances(a)

    fptr.write(str(result) + '\n')

    fptr.close()

