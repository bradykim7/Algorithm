#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the flatlandSpaceStations function below.
def flatlandSpaceStations(n, c): 
    ans=[0]
    c= sorted(c);
    if len(c) >1:   
        for i in range(0,len(c)-1):
            ans.append((c[i+1]-c[i])//2);
    # max( Max distancem, city[0] ~ station[0], city[n-1] ~ station[-1]) First and Final
    return max(max(ans),c[0],n-1-c[-1])
           
            

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    c = list(map(int, input().rstrip().split()))

    result = flatlandSpaceStations(n, c)

    fptr.write(str(result) + '\n')

    fptr.close()

