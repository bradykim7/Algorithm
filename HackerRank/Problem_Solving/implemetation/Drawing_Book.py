#!/bin/python3

import os
import sys

#
# Complete the pageCount function below.
#
def pageCount(n, p):
    #
    # Write your code here.
    #
    t= []
    ans1 =0;
    ans2 =0;
    for i in range(0,n+1,2):
        t.append([i,i+1])
    
    for i in t:
        if p in i:
            break;
        ans1 +=1;

    t.reverse()

    for i in t:
        if p in i:
            break;
        ans2 +=1;

    print(ans1, ans2)    
    if ans2 > ans1:
        return ans1
    else:
        return ans2;    
'''
more easy way to return it
return min(p//2, n//2 - p//2)

'''



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    p = int(input())

    result = pageCount(n, p)

    fptr.write(str(result) + '\n')

    fptr.close()

