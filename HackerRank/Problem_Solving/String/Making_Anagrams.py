#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the makingAnagrams function below.
def makingAnagrams(s1, s2):
    l1 = list(s1);
    l2 = list(s2);
    same =set();
    for i in s1:
        if i in s2:
            same.add(i);

    for i in s1:
        if i in l2:
            l1.remove(i);
            l2.remove(i);
    return len(l1)+len(l2)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s1 = input()

    s2 = input()

    result = makingAnagrams(s1, s2)

    fptr.write(str(result) + '\n')

    fptr.close()
