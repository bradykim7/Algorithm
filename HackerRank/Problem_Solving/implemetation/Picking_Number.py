#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'pickingNumbers' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#

def pickingNumbers(a):
    # Write your code here
    index=[0]*100;
    
    for i in a:
        index[i]+=1;
    ans=0;
    for i in range(len(index)):
        ans = max(ans,index[i])
        if i == 99:
            break;
        ans = max(ans,index[i]+index[i+1])
        
    return ans;
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = pickingNumbers(a)

    fptr.write(str(result) + '\n')

    fptr.close()

