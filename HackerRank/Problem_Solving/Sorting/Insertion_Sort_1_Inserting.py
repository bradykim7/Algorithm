#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the insertionSort1 function below.
def insertionSort1(n, arr):
    temp = arr[n-1]
    for i in range(n-1,0,-1):
        if temp < arr[i-1]:
            arr[i]=arr[i-1]
        elif temp > arr[i-1]:
            arr[i]=temp
            break;
        for i in arr:
            print(i,end=" ")
        print(" ")
    if temp < arr[0]:
        arr[0]=temp;
    for i in (arr):
        print(i, end= " ")
if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    insertionSort1(n, arr)
