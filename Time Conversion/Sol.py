#!/bin/python3

import os
import sys

#
# Complete the timeConversion function below.
#
def timeConversion(s):
    if (s[-1:-3:-1]=="MP"):
        x=int(s[:2])
        x+=12
        print(x,s[2:8],sep="")



s=input()
timeConversion(s)
