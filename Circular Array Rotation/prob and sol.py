# https://www.hackerrank.com/challenges/circular-array-rotation/problem?h_r=next-challenge&h_v=zen

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the circularArrayRotation function below.
def circularArrayRotation(a, k, queries):
    result=[]
    for query in queries:
        result.append(a[query-k % n])
    for i in result:
        print(i)
    
    '''
    Sol 2
    a = a[-k:] + a[:-k]
    for query in queries:
        print(a[query])
    
    Sol1
    n=len(a)
    k=k%n
    while k>0:
        a1=[]
        #print(a,a1)
        a1.append(a[-1])
        #print(a,a1)
        a1[1:]=a[:n-1]
        #print(a,a1)
        #a1.append(a[0])
        #print(a,a1)
        a=a1[:]
        #print(a,a1)
        k-=1
    #print(a,a1)
    for query in queries:
        print(a[query])
    print(a[queries])'''
        

if __name__ == '__main__':
    

    nkq = input().split()

    n = int(nkq[0])

    k = int(nkq[1])

    q = int(nkq[2])

    a = list(map(int, input().rstrip().split()))

    queries = []

    for _ in range(q):
        queries_item = int(input())
        queries.append(queries_item)

    circularArrayRotation(a, k, queries)

    
