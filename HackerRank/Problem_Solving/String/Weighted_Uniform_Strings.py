#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the weightedUniformStrings function below.
def weightedUniformStrings(s, queries):
    ## string problem if you want to reduce the time
    ## when checking overlap part
    query=set();
    ans=[];

    for i in range(len(s)):
        if i==0:
            query.add(ord(s[i])-ord('a')+1);
            count=1;
        elif s[i-1] == s[i]:
            count+=1;
            query.add((ord(s[i])-ord('a')+1)*count);
        else:
            count=1;
            query.add(ord(s[i])-ord('a')+1);

    for i in queries:
        if i in query:
            ans.append('Yes')
        else:
            ans.append('No')
    return ans;
        
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    queries_count = int(input())

    queries = []

    for _ in range(queries_count):
        queries_item = int(input())
        queries.append(queries_item)

    result = weightedUniformStrings(s, queries)

    fptr.write('\n'.join(result))
    fptr.write('\n')

    fptr.close()

