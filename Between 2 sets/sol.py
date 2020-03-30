#!/bin/python3

import sys

n,m = map(int, input().strip().split(' '))
a = list(map(int, input().split()))
b = list(map(int, input().split()))

ausgabe = 0
for q in range(max(a), min(b) +1):
    if all(q % arr == 0 for arr in a) and all(brr % q == 0 for brr in b):
        ausgabe += 1
    
print(ausgabe)

OR-------------------------------------------------------------------------
O(n log(n)) solution.
1. find the LCM of all the integers of array A.
2. find the GCD of all the integers of array B.
3. Count the number of multiples of LCM that evenly divides the GCD.

import sys
from functools import reduce
from fractions import gcd

input()
a = map(int,input().strip().split())
b = map(int,input().strip().split())
lcm_a = reduce(lambda x,y: x*y//gcd(x,y), a)
gcd_b = reduce(gcd, b)
print(sum(1 for x in range(lcm_a,gcd_b+1,lcm_a) if gcd_b%x==0))

