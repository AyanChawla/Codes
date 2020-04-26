#https://www.hackerrank.com/challenges/lisa-workbook/problem


#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the workbook function below.
def workbook(n_ch, mx_pb, pb_per_ch):
    count = 0
    page = 1
    for chapter_problem in problems_in_chapters:
        for current_problem in range(1,chapter_problem + 1):
            if(page == current_problem):
                count = count + 1
            if ((current_problem % k == 0 )or current_problem == chapter_problem):
                page = page + 1
            
    print(count)





if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    arr = list(map(int, input().rstrip().split()))

    workbook(n, k, arr)
