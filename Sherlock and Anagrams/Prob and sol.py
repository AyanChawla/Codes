#https://www.hackerrank.com/challenges/sherlock-and-anagrams/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=dictionaries-hashmaps
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the sherlockAndAnagrams function below.
def sherlockAndAnagrams(s):
    n=len(s)
    ans=0
    for i in range(1,n):
        dct={}
        for j in range(n-i+1):
            subs= "".join(sorted(s[j:j+i]))
            if subs not in dct:
                dct[subs]=1
            else:
                dct[subs]+=1
            ans+=dct[subs]-1
    print(ans)
if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s = input()

        sherlockAndAnagrams(s)

        #fptr.write(str(result) + '\n')

    #fptr.close()
