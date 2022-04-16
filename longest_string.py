# -*- coding: utf-8 -*-
"""
Created on Sun Dec 26 09:20:18 2021

@author: EGBUNA
"""

def longest_string():
    string = input('enter string: ')
    temp = []
    final_temp = []
    for i in range(len(string)):
        for j in range(i, len(string)):
            if string[j] in temp:
                if len(temp) > len(final_temp):
                    final_temp = temp
                temp = []
                
                break
            else:
                temp.append(string[j])
    return final_temp, len(final_temp)

print(longest_string())