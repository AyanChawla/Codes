#https://www.hackerrank.com/challenges/queens-attack-2/problem




# MY SOLUTION-----------------
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the queensAttack function below.
def queensAttack(matrixsize, k, x_q, y_q, obstacles):
    n,s,e,w,n_e,s_e,s_w,n_w=False,False,False,False,False,False,False,False
    extra=[]
    for i in obstacles:
        if i[0]+0*i[1]-x_q==0 and i[1]<y_q:
            w=True
            extra.append(y_q-i[1]-1)
        if i[0]+0*i[1]-x_q==0 and i[1]>y_q:
            e=True
            extra.append(i[1]-y_q-1)
        if 0*i[0]+i[1]-y_q==0 and i[0]<x_q:
            s=True
            extra.append(x_q-i[0]-1)
        if 0*i[0]+i[1]-y_q==0 and i[0]>x_q:
            n=True
            extra.append(i[0]-x_q-1)
        if(x_q-y_q==i[0]-i[1] and i[0]>x_q):
            n_e=True
            extra.append(i[0]-x_q-1)
        if(x_q-y_q==i[0]-i[1] and i[0]<x_q):
            s_w=True
            extra.append(x_q-i[0]-1)
        if(x_q+y_q==i[0]+i[1] and i[0]>x_q):
            n_w=True
            extra.append(i[0]-x_q-1)
        if(x_q+y_q==i[0]+i[1] and i[0]<x_q):
            s_e=True
            extra.append(x_q-i[0]-1)
    #print(sum(extra),matrixsize)
    cnt=sum(extra)
    if n==False:
        for i in range(x_q+1,matrixsize+1):
            cnt+=1
    if s==False:
        for i in range(1,x_q):
            cnt+=1
    if e==False:
        for i in range(y_q+1,matrixsize+1):
            cnt+=1
    if w==False:
        for i in range(1,y_q):
            cnt+=1
    if n_e==False:
        x=x_q
        y=y_q
        while x+1<=matrixsize and y+1<=matrixsize:
            cnt+=1
            x+=1
            y+=1
    if s_w==False:
        x=x_q
        y=y_q
        while x-1>=1 and y-1>=1:
            cnt+=1
            x-=1
            y-=1
    if n_w==False:
        x=x_q
        y=y_q
        while x+1<=matrixsize and y-1>=1:
            cnt+=1
            x+=1
            y-=1
    if s_e==False:
        x=x_q
        y=y_q
        while x-1>=1 and y+1<=matrixsize:
            cnt+=1
            x-=1
            y+=1
    print(cnt)
if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    r_qC_q = input().split()

    r_q = int(r_qC_q[0])

    c_q = int(r_qC_q[1])

    obstacles = []

    for _ in range(k):
        obstacles.append(list(map(int, input().rstrip().split())))

    queensAttack(n, k, r_q, c_q, obstacles)
