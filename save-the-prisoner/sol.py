#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the saveThePrisoner function below.
def saveThePrisoner(prisoner, candies, starting):
    if(candies+starting<prisoner):
        return starting + candies-1
    elif((candies+starting-1)%prisoner==0):
        return prisoner
    else:
        return (candies+starting-1)%prisoner

if __name__ == '__main__':

    t = int(input())

    for t_itr in range(t):
        nms = input().split()

        n = int(nms[0])

        m = int(nms[1])

        s = int(nms[2])

        result = saveThePrisoner(n, m, s)

        print(result)

