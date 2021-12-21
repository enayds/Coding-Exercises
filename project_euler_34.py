# -*- coding: utf-8 -*-
"""
Created on Mon Nov 29 08:29:52 2021

@author: EGBUNA
"""

## creating a factorial function
from math import prod
def Fact(num):
    if num == 1 or num == 0:
        return 1
    else:
        return prod([f + 1 for f in range(num)])


## create a function for checking if the number is a curious number
def Check(num):
    summ = 0
    li = list(str(num))
    for i in li:
        summ += Fact(int(i))
    if summ == num:
        return True
    else:
        return False

answer = 0
for i in range(10, 1499999):
    if Check(i):
        print(i)
        answer += i
print(answer)