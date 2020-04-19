#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the designerPdfViewer function below.
def designerPdfViewer(h, word):
    index=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'];

    cnt = []
    for i in word:
        for j in range(len(index)):
            if i==index[j]:
                cnt.append(j)
    ans= h[0];

    print(cnt)

    for i in cnt:
        if h[i] >=ans:
            ans= h[i]
    return len(word)*ans;        
            

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    h = list(map(int, input().rstrip().split()))

    word = input()

    result = designerPdfViewer(h, word)

    fptr.write(str(result) + '\n')

    fptr.close()

