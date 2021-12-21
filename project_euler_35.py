# -*- coding: utf-8 -*-
"""
Created on Tue Nov 30 09:09:42 2021

@author: EGBUNA

Project Euler problem 35
circular primes
"""
import time
start = time.time()
from math import floor, sqrt
# create a reversing function to reverse our digits

def Reverse(num):
    li = []
    num = str(num)
    for i in range(len(num)):
        num = num[-1] + num[0:-1]
        li.append(int(num))
        # this function will return a list of possible reversed numbers 
    return li

# create a Prime Checking Function to check if a number is a prime
def Check(num):
    for i in range(2,floor(sqrt(num))+ 1):
        if num % i == 0 :
            return False
    else:
        return True

answer = []
for i in range(101,1000000,2):
    if i in answer:
        continue
    else:
        values = Reverse(i)
        counter = 0
        for j in values:
            if Check(j):
                counter += 1
            else:
                break
    if counter == len(values):
        answer.append(i)
print(answer)  
print('time taken =', time.time() - start)