#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the acmTeam function below.
def acmTeam(topic):
    cnt=[];
    for i in range(len(topic)):
        topic[i] = int('0b'+topic[i],2);
    for i in topic[:-1]:
        for j in topic[1+topic.index(i):]:
            cnt.append(bin(i|j))
    ans=[];
    for i in cnt:
        ans.append(i.count('1'));
        
    return max(ans), ans.count(max(ans));

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    topic = []

    for _ in range(n):
        topic_item = input()
        topic.append(topic_item)

    result = acmTeam(topic)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()

