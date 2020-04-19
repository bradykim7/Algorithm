#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the sockMerchant function below.
def sockMerchant(n, ar): 
    check_stack = [] 
    answer = 0 
    # 10 20 20 10 10 30 50 10 20

    for i in range(n): 
        if ar[i] not in check_stack: 
            check_stack.append(ar[i]) 
        else: 
            check_stack.remove(ar[i]) 
            answer = answer + 1 
    return answer

        
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()

