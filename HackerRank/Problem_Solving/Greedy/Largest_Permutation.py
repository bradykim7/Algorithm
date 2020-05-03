#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the largestPermutation function below.
def largestPermutation(k, arr):

    # making the hashmap
    # in python we call hashmap, Dictionary
    c = {}
    n = len(arr)
    for i in range(len(arr)):
        c[arr[i]] = i


    for i in range(len(arr)):
        # checking the how many times can we switch
        if  k == 0:
            break;
        # If array has the largest number in correct place
        if arr[i] == n-i:
            continue;

        # Find largest number
        # ex) c[5-0](value) = 3 (index)
        temp = c[n-i]
        # Swapping first one and the largest number in list
        # ex) c[arr[0]] = c[5]
        # c[5] = 0;
        c[arr[i]] = c[n-i];
        c[n-i] = i;

        # arr[3] = arr[0]
        # arr[0]=  arr[3]
        arr[temp], arr[i] = arr[i], arr[temp]

        k -=1;


    return arr;



if __name__ == '__main__':

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    arr = list(map(int, input().rstrip().split()))

    result = largestPermutation(k, arr)

    print(' '.join(map(str, result)))

