# -*- coding: utf-8 -*-
"""
Created on Tue Nov  9 08:08:11 2021

@author: EGBUNA

project euler problem 29
distinct power

"""
def distinct_power(a, b):
    li = []
    for i in range(2,a+1):
        for j in range(2,b+1):
            mul = i ** j
            if mul not in li:
                li.append(mul)
            else:
                continue
    return len(li)
            
print(distinct_power(100, 100))