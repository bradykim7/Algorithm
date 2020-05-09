#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the superReducedString function below.
def superReducedString(s):
    ans=[];
    for i in s:
        if not ans:
            ans.append(i);
        else:
            if i == ans[-1]:
                ans.pop(-1)
            else:
                ans.append(i);

    if not ans:
        return 'Empty String'
    else:
        c=''
        for i in ans:
            c+=i;
        return c;

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = superReducedString(s)

    fptr.write(result + '\n')

    fptr.close()

