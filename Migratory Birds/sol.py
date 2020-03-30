#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the migratoryBirds function below.
def migratoryBirds(arr):
    st=set(arr)
    arr1=list(st)
    mx=0
    for i in arr1:
        if(arr.count(i)>mx):
            res=i
            mx=arr.count(i)
    return res
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = migratoryBirds(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
    
    
    
    
    ---------------------------------____ALTERNATE
    
    print(sorted(reversed(sorted(set(types))), key=types.count)[-1])
