# -*- coding: utf-8 -*-
"""
Created on Tue Feb  4 20:15:36 2020

@author: Aleks
"""

def function_1(x): 
    return x**1
def function_2(x): 
    return x**2
def function_3(x): 
    return x**3
def function_4(x): 
    return x**4
def function_5(x): 
    return x**5


callbac = [function_1, function_2, function_3, function_4, function_5]

print ('\nNamed Functions')
for f in callbac: 
    print('Result:', f(5.8766))


