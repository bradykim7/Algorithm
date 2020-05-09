#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the alternate function below.
def alternate(s):

    temp = list(set(s));
    c=[];
    for i in range(0,len(temp)-1):
        for j in range(i+1,len(temp)):
            c.append([temp[i],temp[j]]);
    pre=0;

    for i in range(len(c)):
        ml = s;
        flag =0;
        for j in range(len(s)):
            if s[j] not in c[i]:
                ml=ml.replace(s[j],'')

        for k in range(0,len(ml)-1):
            if ml[k] == ml[k+1]:
                flag=1;
                break;

        if flag == 0:
            if i == 0:
                pre=len(ml);
            else:
                if len(ml) > pre:
                    pre = len(ml);
    return pre



    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    l = int(input().strip())

    s = input()

    result = alternate(s)

    fptr.write(str(result) + '\n')

    fptr.close()

