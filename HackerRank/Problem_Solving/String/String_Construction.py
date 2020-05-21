#!/bin/python3
import math
import os
import random
import re
import sys

# Complete the stringConstruction function below.
def stringConstruction(s):
    count =0;
    p = set();
    for i in s:
        if i in p:
            continue;
        p.add(i);
        count+=1;


    return (count)
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = stringConstruction(s)

        fptr.write(str(result) + '\n')

    fptr.close()
