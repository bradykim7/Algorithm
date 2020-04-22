#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the kaprekarNumbers function below.
def kaprekarNumbers(p, q):
    ans=[]
    for i in range(p,q+1):
        n = i;
        d = len(str(n))
        qn = n*n;
        dd = len(str(qn));

        l= str(qn)[:dd-d];
        r= str(qn)[-d:];

        if l =="":
            l='0';

        if int(l)+int(r) == n:
            ans.append(i);
    if not ans:
        print("INVALID RANGE");
    else:
        for i in ans:
            print(i, end=" ")

if __name__ == '__main__':
    p = int(input())

    q = int(input())

    kaprekarNumbers(p, q)

