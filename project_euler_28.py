# -*- coding: utf-8 -*-
"""
Created on Tue Nov  9 07:40:18 2021

@author: EGBUNA


project euler problem 28
number spiral diagnosis

"""
def spiral(limit):
    summ =  1
    total = 1
    diff = 2
    while summ < limit:
        for i in range(4):
            summ += diff
            total += summ
        diff += 2
    return summ, total

print(spiral(100*100))