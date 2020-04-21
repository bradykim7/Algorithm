#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the saveThePrisoner function below.
def saveThePrisoner(n, m, s):
    # n == the number of prisoners
    # m == the number of candies
    # s == starting number of prisoner
    # Think that starting number is s and it should be counted so we have to substract 1
    # ex) 5 8 3  => 3 4 5 6(1) 7(2) 8(3) 9(4) 10(5) 
    # remain == 0 means the number of last prisoner
    remain = (s+m-1)%n;
    if remain == 0:
        return n;
    else:
        return remain;

    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        nms = input().split()

        n = int(nms[0])

        m = int(nms[1])

        s = int(nms[2])

        result = saveThePrisoner(n, m, s)

        fptr.write(str(result) + '\n')

    fptr.close()

