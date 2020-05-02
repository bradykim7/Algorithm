#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the decentNumber function below.
def decentNumber(N):
    # counting the number of '3' 
    # 규칙이 보면 33333 이 패턴이 들어가는 숫자가 2 1 0 으로 반복
    # 따라서 나머지가 2 1 0 으로 나오게 만드는함수는 
    # ((M-1)*N)%M 이다. 문제의 경우 3으로 나누는 나머지를 구하는 것
    K = 5*((2*N)%3)

    if K > N:
        return -1
    else:
        return '5' * (N-K) + '3'*K


if __name__ == '__main__':
    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        print(decentNumber(n))

