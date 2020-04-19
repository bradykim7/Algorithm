#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the migratoryBirds function below.
def migratoryBirds(arr):
    bird = [0,0,0,0,0];
    for i in range(len(arr)):
        if i == len(arr):
            break;
        if arr[i]==1:
            bird[0]+=1;
        elif arr[i]==2:
            bird[1]+=1;
        elif arr[i]==3:
            bird[2]+=1;
        elif arr[i]==4:
            bird[3]+=1;
        else:
            bird[4]+=1;

    m = max(bird);
    for i in range(len(bird)):      
        if m == bird[i]:
            return i+1;

       


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = migratoryBirds(arr)

    fptr.write(str(result) + '\n')

    fptr.close()

