# -*- coding: utf-8 -*-
"""
Created on Sat Nov 13 11:40:18 2021

@author: EGBUNA

Project Euler 
problem 5
1001 prime

"""

from math import floor, sqrt
def check(n):
    for i in range(3, floor(sqrt(n)) + 1):
        if n % i == 0:
            return False
    else:
        return True

def Check(num):
    for i in range(2,floor(sqrt(num))+ 1):
        if num % i == 0 :
            return False
    else:
        return True

counter = 0
i = 3
while counter < 1002:
    if check(i):
        counter += 1
    i += 2
print(i)