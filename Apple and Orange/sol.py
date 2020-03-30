#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countApplesAndOranges function below.
def countApplesAndOranges(s, t, a, b, apples, oranges):
    cnt_a=cnt_o=0
    for i in range(len(apples)):
        if((a+apples[i])>=s and (a+apples[i])<=t):
            cnt_a+=1
    for i in range(len(oranges)):
        if((b+oranges[i])>=s and (b+oranges[i])<=t):
            cnt_o+=1
    print(cnt_a,cnt_o,sep="\n")

if __name__ == '__main__':
    st = input().split()

    s = int(st[0])

    t = int(st[1])

    ab = input().split()

    a = int(ab[0])

    b = int(ab[1])

    mn = input().split()

    m = int(mn[0])

    n = int(mn[1])

    apples = list(map(int, input().rstrip().split()))

    oranges = list(map(int, input().rstrip().split()))

    countApplesAndOranges(s, t, a, b, apples, oranges)
