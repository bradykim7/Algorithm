#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the jimOrders function below.
def jimOrders(orders):
    # Using the ways to sorting dictionary
    # because I want to get a index nubmer of orders
    ans=[]
    temp={}
    c=[]
    for i,j in orders:
        c.append(i+j);
    for i in range(len(c)):
        temp[i+1]=c[i];

    c = sorted(temp.items(), key=lambda x:x[1]);
    for i,j in c:
        ans.append(i);
    return(ans)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    orders = []

    for _ in range(n):
        orders.append(list(map(int, input().rstrip().split())))

    result = jimOrders(orders)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
