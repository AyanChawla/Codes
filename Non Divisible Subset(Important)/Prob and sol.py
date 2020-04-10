#https://www.hackerrank.com/challenges/non-divisible-subset/problem?h_r%5B%5D%5B%5D=next-challenge&h_r%5B%5D%5B%5D=next-challenge&h_r%5B%5D%5B%5D=next-challenge&h_r%5B%5D%5B%5D=next-challenge&h_r%5B%5D%5B%5D=next-challenge&h_v%5B%5D%5B%5D=zen&h_v%5B%5D%5B%5D=zen&h_v%5B%5D%5B%5D=zen&h_v%5B%5D%5B%5D=zen&h_v%5B%5D%5B%5D=zen&isFullScreen=false&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen
# LOGIC-----------------------------
'''
here's the logic complete which follows BigO(n) complexity of the algorithm suppose let's say u give input 10 13 where K=13 and the values are : 2375782 21836421 2139842193 2138723 23816 21836219 2948784 43864923 283648327 23874673.

Now the main logic behind this is if:

(a+b)%K=0(means evenly divisible) then (a%k+b%K=K)

Hence, we take first take the remainders of all the input integers by dividing them with K, In this case we divide all the integers by K=13 which gives us the following set of remainders:

6 9 8 2 0 2 7 11 1 4

now look carefully in the remainder set,

i.) 11+2=13=K thus, we cannot have both 11 and 2 , we must select one of them based on the higher frequency, in this case 2 has a higher frequency than 11 so SELECT all the 2s

ii.) 7+6=13=K thus, we cannot have both 7 and 6 , we must select one of them based on the higher frequency, in this case 6 and 7 both have equal frequencies so select any one of them, let's say(we select 6)

iii.) 9+4=13=k thus, we cannot have both 9 and 4 , we must select one of them based on the higher frequency, in this case 9 and 4 both have equal frequencies so select any one of them, let's say(we select 9)

now we are left with remainders 1,8,0
so the final subset of remainders comes out to be

[6,9,2,2,1,8,0]
the length of this subset is the answer which is"7"

Hope this helps:)
also there are two special cases

1.)if k=0 then return 1 since none will be divisible

2.)if k=1 then return 1 since all the numbers will be divisible

'''

# SOLUTION ------------------------
#!/bin/python3

import math
import os
import random
import re
import sys           

# Write your code here

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    s = list(map(int, input().rstrip().split()))

    #nonDivisibleSubset(k, s)
    remainder_array = [i % k for i in s]
    check_array = []
    for i in set(remainder_array):
        if k-i not in check_array:
            check_array.append(i)
    print(sum([1 if i==0 or i*2==k else max(remainder_array.count(i),remainder_array.count(k-i)) for i in check_array]))
