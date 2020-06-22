#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the checkMagazine function below.
def checkMagazine(magazine, note):
    c={}
    for i in magazine:
        c[i] = 0

    for i in magazine:
        if i in c:
            c[i]+=1

    for i in note:
        if i not in magazine:
            print('No')
            return

        if i in c:
            c[i]-=1
            if c[i] < 0:
                print('No')
                return
    print('Yes')

if __name__ == '__main__':
    mn = input().split()

    m = int(mn[0])

    n = int(mn[1])

    magazine = input().rstrip().split()

    note = input().rstrip().split()

    checkMagazine(magazine, note)
