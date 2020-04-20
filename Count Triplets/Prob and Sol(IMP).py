#https://www.hackerrank.com/challenges/count-triplets-1/problem?h_l=interview&playlist_slugs%5B%5D=virtusa

#-----------------------------------SOLUTION_________________________________
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countTriplets function below.
def countTriplets(arr, r):
    a = 0
    cpairs = dict()
    cnumber = dict()
    for i in reversed(arr):
        #print("i is {} at the start of loop".format(i))
        if i*r in cpairs:
            #print("{}*{} in {}".format(i,r,cpairs))
            #print("BEFORE cpairs[{}*{}]={} and a={}".format(i,r,cpairs[i*r],a))
            a += cpairs[i*r]
            #print("AFTER cpairs[{}*{}]={} and a={}".format(a,i,r,cpairs[i*r],a))

        if not(i in cnumber):
            #print("{} is adding to cnumber".format(i))
            cnumber[i] = 0

        if i*r in cnumber:
            if i in cpairs:
                #print("BEFORE cpairs[{}] and cnumber[{}*{}]={}".format(i,i,r,cnumber[i*r]))
                cpairs[i] += cnumber[i*r]
                #print("AFTER cpairs[{}]={} and cnumber[{}*{}]={}".format(i,cpairs[i],i,r,cnumber[i*r]))
            else:
                #print("BEFORE ELSE cpairs[{}] and cnumber[{}*{}]={}".format(i,i,r,cnumber[i*r]))
                cpairs[i] = cnumber[i*r]
                #print(" AFTER ELSE cpairs[{}]={} and cnumber[{}*{}]={}".format(i,cpairs[i],i,r,cnumber[i*r]))
        #print("BEFORE {}".format(cnumber[i]))
        cnumber[i] += 1
        #print(cnumber,cpairs)

    return a


if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nr = input().rstrip().split()

    n = int(nr[0])

    r = int(nr[1])

    arr = list(map(int, input().rstrip().split()))

    countTriplets(arr, r)
