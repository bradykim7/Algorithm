#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the bigSorting function below.

def bigSorting(unsorted):
    # For Python 3 !
    # In this case, the input is the string
    # And most of us can think that we have to convert string to int
    # But that costs pretty much time so Key point is
    # First just sort the array and Second sorting with len of items;
    return (sorted(sorted(unsorted),key=len))


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    unsorted = []

    for _ in range(n):
        unsorted_item = input()
        unsorted.append((unsorted_item))

    result = bigSorting(unsorted)

    fptr.write('\n'.join(result))
    fptr.write('\n')

    fptr.close()
