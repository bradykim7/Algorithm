#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the howManyGames function below.
def howManyGames(p, d, m, s):
    # Return the number of games you can buy
    budget= s;
    ans=0;
    i =0;
    while budget >=0:
        money = p-d*i;
        if money >= m:
            budget = budget-money
            ans+=1
        else :
            budget-=m
            ans+=1
        i+=1;
    return ans-1;
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    pdms = input().split()

    p = int(pdms[0])

    d = int(pdms[1])

    m = int(pdms[2])

    s = int(pdms[3])

    answer = howManyGames(p, d, m, s)

    fptr.write(str(answer) + '\n')

    fptr.close()

