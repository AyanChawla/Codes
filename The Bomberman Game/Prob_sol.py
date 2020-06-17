# https://www.hackerrank.com/challenges/bomber-man/problem
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the bomberMan function below.
def bomberMan(n, grid):
    #print("entery")
    row=len(grid)
    #print(grid)
    col=len(grid[0])
    matrix=[["0"]*col for i in range(row)]
    if n%3==1:
        return grid
    elif n%3==2:
        return matrix
    else:
        #print("entery in else")
        for i in range(row):
            for j in range(col):
                #print(grid[i][j])
                if grid[i][j]!=".":
                    #print("jdn")
                    matrix[i][j]="."
                    try:
                        if i+1>=0 and j>=0:
                            matrix[i+1][j]="."
                    except:
                        pass
                    try:
                        if i-1>=0 and j>=0:
                            matrix[i-1][j]="."
                    except:
                        pass
                    try:
                        if i>=0 and j+1>=0:
                            matrix[i][j+1]="."
                    except:
                        pass
                    try:
                        if i>=0 and j-1>=0:
                            matrix[i][j-1]="."
                    except:
                        pass
                    #print(matrix[i][j])
        return matrix

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    rcn = input().split()

    r = int(rcn[0])

    c = int(rcn[1])

    n = int(rcn[2])

    grid = []

    for _ in range(r):
        grid_item = input()
        grid.append(grid_item)

    result = bomberMan(n, grid)
    for i in range(r):
        for j in range(c):
            print(str(result[i][j]),end="")
        print()
    #result1=[]
    #for i in range(r):
    #    result1.append("".join(result[i]))
#
    #fptr.write('\n'.join(result1))
    #fptr.write('\n')
#
    #fptr.close()
