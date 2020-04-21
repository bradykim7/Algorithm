#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the cutTheSticks function below.
def cutTheSticks(arr):
    ans=[]; m=[];
    for i in arr:
        if i in m:
            continue;
        else:
            m.append(i);
    m.sort(); 
    for i in m:
        cnt=0;
        for j in arr:
            if j-i >=0:
                cnt+=1;
        ans.append(cnt);

    return ans;                
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = cutTheSticks(arr)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()

