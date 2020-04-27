#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the gridChallenge function below.
def gridChallenge(grid):
    c =[]
    # sorting line 
    for i in grid:
        w=''
        for j in sorted(i):
            w+=j;
        c.append(w)
    print(c)
    # compare vertically
    for i in range(len(c[0])):
        for j in range(len(c)):
            if j == len(c)-1:
                continue;
            if c[j][i] > c[j+1][i]:
                return 'NO'
    return 'YES'        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        n = int(input())

        grid = []

        for _ in range(n):
            grid_item = input()
            grid.append(grid_item)

        result = gridChallenge(grid)

        fptr.write(result + '\n')

    fptr.close()

