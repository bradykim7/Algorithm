#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the sherlockAndAnagrams function below.
def sherlockAndAnagrams(s):
        ans = 0
        c = {}
        for i in range(len(s)):
            for j in range(len(s) - i):
                s1 = ''.join(sorted(s[j:j + i + 1]))
                c[s1] = c.get(s1, 0) + 1

        for key in c:
            ans += (c[key] - 1) * c[key] // 2
        return(ans)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = sherlockAndAnagrams(s)

        fptr.write(str(result) + '\n')

    fptr.close()
