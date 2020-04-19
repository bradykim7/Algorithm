#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the miniMaxSum function below.
def miniMaxSum(arr):
    ar =[]
    t=0;
    for i in range(len(arr)):
        t += arr[i];

    for i in range(len(arr)):
        ar.append(t-arr[i]);

    mini =ar[0];
    maxi =ar[0];    
    for i in range(len(ar)):
        if(mini > ar[i]):
            mini= ar[i]
        if(maxi < ar[i]):
            maxi= ar[i]    


    print("%d %d" %(mini, maxi));   
        



if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)

