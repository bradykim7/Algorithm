#!/bin/python3

import math
import os
import random
import re
import sys
# fucking idiot output system in hackerrank 
# Complete the cavityMap function below.
def cavityMap(grid):
    for i in range(1,len(grid)-1):
        for j in range(1,len(grid)-1):
                t=grid[i-1][j];
                b=grid[i+1][j];
                c=grid[i][j];
                l=grid[i][j-1];
                r=grid[i][j+1];
                if t!='X' and b!='X' and c!='X' and l!='X' and r !='X' and c> t and c>b and c>l and c>r:
                    grid[i][j]='X';
    return grid
if __name__ == '__main__':
    n = int(input())

    grid = []

    for _ in range(n):
        grid_item = list(map(int,input()))
        grid.append(grid_item)

    result = cavityMap(grid)
    for i in (result):
        for j in i:
            print(j,end="")
        print(end='\n')


