# -*- coding: utf-8 -*-
"""
Created on Tue Nov  9 08:43:21 2021

@author: EGBUNA

project euler problem 30
digit fifth power

"""
def digit_power(power, start, finish):
    final = []
    for i in range(start, finish):
        li = list(str(i))
        summ = 0
        for j in li:
            summ += int(j) ** power 
        if summ == i:
            final.append(summ)
    return sum(final), final

print(digit_power(5, 1000, 1000000))
