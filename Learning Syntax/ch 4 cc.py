# -*- coding: utf-8 -*-
"""
Created on Tue Feb  4 12:56:52 2020

@author: Aleks
"""
num = input('Enter An Integer:')
def square(num):
    if not num.isdigit():
        return 'Invalid Entry'   
    num = int(num)
    return num*num
print (num, 'Squared Is:', square(num))