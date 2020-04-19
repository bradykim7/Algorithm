#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countingValleys function below.
def countingValleys(n, s):
    pre =0;
    aft =0;
    ans= 0;
    for i in s:
        if i == "U":
            pre = aft;
            aft +=1;
        else:
            pre = aft;
            aft -=1;
            if (pre*aft) <0 or pre==0:
                ans+=1; 
    return ans;               
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    s = input()

    result = countingValleys(n, s)

    fptr.write(str(result) + '\n')

    fptr.close()
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countingValleys function below.
def countingValleys(n, s):
    pre =0;
    aft =0;
    ans= 0;
    for i in s:
        if i == "U":
            pre = aft;
            aft +=1;
        else:
            pre = aft;
            aft -=1;
            if (pre*aft) <0 or pre==0:
                ans+=1; 
    return ans;               
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    s = input()

    result = countingValleys(n, s)

    fptr.write(str(result) + '\n')

    fptr.close()

