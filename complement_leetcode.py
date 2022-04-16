# -*- coding: utf-8 -*-
"""
Created on Tue Dec 28 10:50:59 2021

@author: EGBUNA
"""

class Solution(object):
    def findComplement(self, num):
        if num < 1:
            return 0
        elif num == 2:
            return 1
        else:
            rem = ''
            while True:
                rem = rem + str(num % 2)
                num = num // 2
                if num == 0:
                    break
            rem = rem[::-1]
            comp = ''
            for i in rem:
                if i == '0':
                    comp = comp + '1'
                else:
                    comp = comp + '0'
            summ = 0
            power = 0
            for i in str(comp):
                pows = (len(str(rem)) - power)-1
                summ += int(i)* (2 ** pows)
                power += 1
        return summ
    
answer = Solution().findComplement(5)
print(answer)