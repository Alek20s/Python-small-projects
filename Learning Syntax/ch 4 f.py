# -*- coding: utf-8 -*-
"""
Created on Tue Feb  4 21:27:38 2020

@author: Aleks
"""

def fibonacci_generator():
    a=b=1
    while True:
        yield a
        a,b =b, a+b
        
fib = fibonacci_generator()
for i in fib:
    if i>10000:
        break
    else:
        print ('Generated', i)