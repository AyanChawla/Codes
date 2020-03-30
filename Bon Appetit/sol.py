#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the bonAppetit function below.
def bonAppetit(bill, k, b):
    for i in range(len(bill)):
        if i==k:
            bill[i]=0
    #print(bill)
    if(b==(sum(bill)/2)):
        print("Bon Appetit")
    else:
        print(b-int((sum(bill)/2)))
        

if __name__ == '__main__':
    nk = input().rstrip().split()

    n = int(nk[0])

    k = int(nk[1])

    bill = list(map(int, input().rstrip().split()))

    b = int(input().strip())

    bonAppetit(bill, k, b)
