#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the hackerrankInString function below.
def hackerrankInString(s):
    temp =list('hackerrank');
    ans='';
    j=0
    for i in s:
        if i in temp[j]:
            ans+=i;
            j+=1;
    
        if ans == 'hackerrank':
            return 'YES';
    return 'NO';
            

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = hackerrankInString(s)

        fptr.write(result + '\n')

    fptr.close()

