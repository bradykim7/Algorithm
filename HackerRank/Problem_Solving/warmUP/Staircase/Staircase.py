#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the staircase function below.
def staircase(n):
    x= ' ';
    for i in range(n,0,-1):
        for j in range(i-1,0,-1):
            print(x, end="")
        for j in range(0,n-i+1,1):
            print("#", end="")
        print("")        

if __name__ == '__main__':
    n = int(input())

    staircase(n)

