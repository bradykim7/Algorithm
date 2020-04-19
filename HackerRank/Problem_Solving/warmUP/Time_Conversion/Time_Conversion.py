#!/bin/python3

import os
import sys

#
# Complete the timeConversion function below.
#
def timeConversion(s):
    # make array 
    time = s.split(":")
    # check PM 
    if s[-2:] == "PM":
        # Cause don't need to change
        if time[0] != "12":
            # time[0]== 07 
            time[0] = str(int(time[0])+12)
    else:
        if time[0] == "12":
            time[0] = "00"
    result = ':'.join(time)
    # except PM or AM
    return (result[:-2])
    
if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    f.write(result + '\n')

    f.close()

