#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the plusMinus function below.
def plusMinus(arr):
    ps=0
    ng=0
    x=len(arr)
    for i in arr:
        if i>0:
            ps+=1
        if i<0:
            ng+=1
    zr=x-(ps+ng)
    print(round(ps/x, 6),round(ng/x,6),round(zr/x, 6),sep="\n")
if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
############################################## ALTERNATE
def plusMinus(arr):
    # Complete this function
    positive = sum(x > 0 for x in arr) / len(arr)
    negative = sum(x < 0 for x in arr) / len(arr)
    zero = sum(x == 0 for x in arr) / len(arr)
    
    print(positive, negative, zero, sep="\n")
