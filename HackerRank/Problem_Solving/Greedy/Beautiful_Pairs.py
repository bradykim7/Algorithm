#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the beautifulPairs function below.
def beautifulPairs(A, B):
    ans =0;
    A.sort();B.sort();
    c =[];
    for i in range(len(A)):
        for j in range(len(B)):
            if j in c:
                continue;
            elif A[i] == B[j]:
                ans+=1;
                c.append(j);
                break; 
    #if len(A)- ans >= 1:
     #   return ans+1;
    if len(A)-ans == 0:
        return ans -1;
    else:
        return ans+1;

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    A = list(map(int, input().rstrip().split()))

    B = list(map(int, input().rstrip().split()))

    result = beautifulPairs(A, B)

    fptr.write(str(result) + '\n')

    fptr.close()

