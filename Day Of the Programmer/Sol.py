#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the dayOfProgrammer function below.
def dayOfProgrammer(year):
    if(year>=1919):
        if((year%400==0) or (year%4==0 and not(year%100==0))):
            print("12.09.",year,sep="")
        else:
            print("13.09.",year,sep="")
    elif(year<=1917 and year>=1700):
        if (year%4==0):
            print("12.09.",year,sep="")
        else:
            print("13.09.",year,sep="")
    else:
        print("26.09.1918")



            

if __name__ == '__main__':

    year = int(input().strip())

    result = dayOfProgrammer(year)

-------------------------------------------ALTERNATE
if(year==1918) {
        return "26.09.1918";
    }
    else if((year<1918 && year%4==0) ||(year>1918  &&(year%4==0 && year%100 !=0 || year%400==0))) {
        return "12.09." + year;
    }
    else {
        return "13.09." + year;
    }

