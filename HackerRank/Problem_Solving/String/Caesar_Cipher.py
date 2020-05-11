#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the caesarCipher function below.
def caesarCipher(s, k):
    a =list('abcdefghijklmnopqrstuvwxyz');
    A = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    c=[];C=[]
    for i in range(len(a)):
        c.append(a[(i+k)%len(a)])
    for i in range(len(A)):
        C.append(A[(i+k)%len(A)])
    ans ='';
    for i in s:
        if i in c:
            ans+= c[a.index(i)];
        elif i in C:
            ans+=C[A.index(i)];
        else:
            ans+=i;

    return (ans);
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    s = input()

    k = int(input())

    result = caesarCipher(s, k)

    fptr.write(result + '\n')

    fptr.close()

