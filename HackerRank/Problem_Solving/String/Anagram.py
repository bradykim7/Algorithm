#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the anagram function below.
def anagram(s):
    ans = -1;
    halflength = len(s)//2
    t1,t2={},{};

    # odd number;
    if len(s)%2==1:
        return ans;
    # even number
    left= list(s[:halflength]);
    right= list(s[halflength:]);

    for i in left:
        if i in right:
            right.remove(i);
    ans = len(right);
    return ans;


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = anagram(s)

        fptr.write(str(result) + '\n')

    fptr.close()
