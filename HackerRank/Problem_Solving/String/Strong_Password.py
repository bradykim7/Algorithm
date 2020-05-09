#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumNumber function below.
def minimumNumber(n, password):
    # Return the minimum number of characters to make the password strong
    # least 6, one digit, one upper, one lower, one special
    numbers = "0123456789"
    lower_case = "abcdefghijklmnopqrstuvwxyz"
    upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    special_characters = "!@#$%^&*()-+"
    f =[0,0,0,0];
    ans=0;
    for i in password:
        if i in numbers:
            f[0]=1;
        elif i in lower_case:
            f[1]=1;
        elif i in upper_case:
            f[2]=1;
        elif i in special_characters:
            f[3]=1;
    for i in f:
        if i ==0:
            ans+=1;


    if len(password)+ans <6:
        ans += 6-(len(password)+ans);
        return ans;
    else:
        return ans;

    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    password = input()

    answer = minimumNumber(n, password)

    fptr.write(str(answer) + '\n')

    fptr.close()

