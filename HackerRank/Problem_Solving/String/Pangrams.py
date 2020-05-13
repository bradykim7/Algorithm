#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the pangrams function below.
def pangrams(s):
    temp =list('abcdefghijklmnopqrstuvwxyz');
    Temp = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    for i in s:
        if i.lower() in temp:
            temp.pop(temp.index(i.lower()));

        if not temp:
            return 'pangram';
    return 'not pangram'

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = pangrams(s)

    fptr.write(result + '\n')

    fptr.close()

