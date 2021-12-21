# -*- coding: utf-8 -*-
"""
Created on Mon Nov 29 19:38:21 2021

@author: EGBUNA
"""

def Check(num, dem):
    new_num, new_dem = list(str(num)), list(str(dem))
    if new_num[-1] == new_dem[-1]:
        return '0','0'
    for i in new_num:
        if i in new_dem:
            new_dem.remove(i), new_num.remove(i)
            return new_num, new_dem
    return new_num, new_dem

numerator, denominator = 1,1
for i in range(10, 100):
    for j in range(10,100):
        if i == j:
            continue
        else:
            a , b = Check(i, j)
            if len(a) == 2 or len(b) == 2:
                continue
            elif a[0] == '0' or b[0] == '0':
               continue 
            else:
                di = int(a[0]) / int(b[0])
                if di == i/j and di < 1:
                    numerator *= i
                    denominator *= j
                else:
                    continue