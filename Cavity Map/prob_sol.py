# https://www.hackerrank.com/challenges/cavity-map/problem

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the cavityMap function below.
def cavityMap(grid,n):
    #print(grid)
    grid1= [row[:] for row in grid]
    #print(grid1)
    for i in range(1,n-1):
        for j in range(1,n-1):
            if int(grid[i][j])>int(grid[i][j+1]) and int(grid[i][j])>int(grid[i][j-1]) and int(grid[i][j])>int(grid[i-1][j]) and int(grid[i][j])>int(grid[i+1][j]):
                grid1[i][j]="X"
    for i in grid1:
        print(*i,sep="")


if __name__ == '__main__':
    n = int(input())

    grid = []

    for _ in range(n):
        grid_item = list(map(int,input()))
        grid.append(grid_item)

    cavityMap(grid,n)
