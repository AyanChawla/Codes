
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the breakingRecords function below.
def breakingRecords(scores):
    mn=mx=scores[0]
    cnt=[0,0]
    for i in range(1,len(scores)):
        if scores[i]>mx:
            mx=scores[i]
            cnt[0]+=1
        if scores[i]<mn:
            mn=scores[i]
            cnt[1]+=1
    return cnt

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
