# -*- coding: utf-8 -*-
"""
Created on Mon Nov  8 20:40:12 2021

@author: EGBUNA
"""

''' project euler problem 27
longest quadratic primes
'''

#making a function to check if a number is prime or not
def prime_check(n):
    for i in range(2, n):
        if n% i == 0:
            return False
        else:
            continue
    return True


# making a function to fetch the list prime numbers

def prime(n):
    li = []
    for i in range(n):
        if prime_check(i):
            li.append(i)
        else:
            continue
    return li


## the main program

a = [i for i in range(-999,1000,2)]
b = prime(1001)
max_n, max_a,max_b = 0,0,0

for i in a:
    print(i)
    for j in b:
        n = 0
        while True:
            test = n ** 2 + i*n + j
            if prime_check(test):
                n += 1
            else:
                break
        if n > max_n:
            max_n = n
            max_a = i
            max_b = j
        

print('max_n =', max_n, 'max_a = ', max_a, 'max_b =', max_b)









# -*- coding: utf-8 -*-
"""
Created on Wed Nov 10 17:27:04 2021

@author: EGBUNA
"""

import math 
import time

start = time.time()
def isPrime(num):
    prime = True
    if num < 2: return False 
    if num == 2: return True
    for factor in range(3, int(math.sqrt(num)), 2):
        if num % factor == 0: prime = False
    return prime

def testEquation(a,b):
    n = 0
    while True:
        test = n ** 2 + a*n + b
        if isPrime(test):
            n += 1
        else:
            break
    return n

best = 0
besta = 0
bestb = 0
for a in range (-1000, 1001):
    for b in range(1, 1000):
        c = testEquation(a, b)
        if c > best:
            best, besta, bestb = c, a, b
print(besta * bestb, time.time() - start)


