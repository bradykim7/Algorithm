#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the palindromeIndex function below.
def palindromeIndex(s):
    a, b = 0, len(s)-1
    res = -1;
    if a == b:
        return res;

    while a != b:
        # Ending point
        if a == len(s)-1 or b == 0:
            break;
        # checking right and left character is same
        if s[a] == s[b]:
            a, b = a+1 , b-1
        # s
        else:
            # a b c b a f
            if s[a] == s[b-1] and s[a+1] == s[b-2]:
                res = b;
                break;
            else :
                res = a;
                break;

    return res


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = palindromeIndex(s)

        fptr.write(str(result) + '\n')

    fptr.close()
