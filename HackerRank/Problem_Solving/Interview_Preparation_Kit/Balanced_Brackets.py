#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the isBalanced function below.
def isBalanced(s):
    c=[]
    for i in s:
        if i == ')':
            if len(c) ==0:
                return 'NO'
            elif c[-1] == '(':
                c.pop()
            else:
                return 'NO'
        elif i ==']':
            if len(c) ==0:
                return 'NO'
            elif c[-1] == '[':
                c.pop()
            else:
                return 'NO'
        elif i == '}':
            if len(c) ==0:
                return 'NO'
            elif c[-1] == '{':
                c.pop()
            else:
                return 'NO'
        else:
            c.append(i)

    if len(c) == 0:
        return 'YES'
    else:
        return 'NO'


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        s = input()

        result = isBalanced(s)

        fptr.write(result + '\n')

    fptr.close()
