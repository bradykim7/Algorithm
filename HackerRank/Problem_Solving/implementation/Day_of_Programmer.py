#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the dayOfProgrammer function below.
def dayOfProgrammer(year):
    # 256th day == programmer's day
    # 1919 ~ 2700
    # not leap == 13.09.xxxx
    # leap == 12.09.xxxx 

    # 1918
    # 256th = 26.09.1918

    # 1700 ~ 1917
    # not leap = 13.09.xxxx
    # leap = 12.09.xxxx
    if year >= 1919 and year <= 2700:
        if year%4 ==0 and year%100 != 0:
            return '12.09.'+str(year);
        elif year%400==0:
            return '12.09.'+str(year);
        else:
            return '13.09.'+str(year);

    elif year >= 1700 and year <1918:
        if year%4 ==0 :
            return '12.09.'+str(year);
        else:
            return '13.09.'+str(year);

    elif year == 1918:
        return '26.09.1918';


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    year = int(input().strip())

    result = dayOfProgrammer(year)

    fptr.write(result + '\n')

    fptr.close()

