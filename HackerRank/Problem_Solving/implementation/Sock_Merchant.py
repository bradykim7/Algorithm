#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    
    num = [];
    ans = 0;


    for i in ar:
        if i not in num:
            num.append(i);
    
    for i in num:
        index= 0;
        for j in ar:
            if i ==j:
                index+=1;
        ans += int(index/2)        

    return ans;    



        
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()

