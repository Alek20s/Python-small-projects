# -*- coding: utf-8 -*-
"""
Created on Tue Feb 18 21:14:08 2020

@author: Aleks
"""

from random import random, sample
num = random()

print ('Random Float 0.0 -1.0:', num)

num = int(num*10)
print('Random Integer 0 - 9:', num)

nums = []; i=0
while i<6:
    nums.append(int(random()*10) + 1)
    i +=1
print('Random Multiple Integers 1-10:', nums)

nums = sample(range(1,100000000000),30000)
print('Random Integer Sample 1 - 59:', nums)










