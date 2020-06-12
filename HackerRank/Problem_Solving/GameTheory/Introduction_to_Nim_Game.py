# Before you solve this problem you must watch this video in youtube. Amazing When is first.
# https://www.youtube.com/watch?v=ORaGSyewF9Q
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the nimGame function below.
def nimGame(pile):
    f = pile[0]
    for i in range(len(pile)):
        if i == 0 :
            p = pile[i]
            continue
        else:
            p = p^pile[i]
    if p == 0:
        return "Second"
    else:
        return "First"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    g = int(input())

    for g_itr in range(g):
        n = int(input())

        pile = list(map(int, input().rstrip().split()))

        result = nimGame(pile)

        fptr.write(result + '\n')

    fptr.close()
