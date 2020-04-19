# -*- coding: utf-8 -*-
"""
Created on Sun Feb  9 20:36:04 2020

@author: Aleks
"""

import math, random
print ('Rounded Up 9.5:', math.ceil(9.5))
print ('Rounded Up 9.5:', math.floor(9.5))

num =4 
print (num, 'Squared', math.pow(num,2))
print (num, 'Square Root', math.sqrt(num))

nums = random.sample(range(-31,59),10)
print ('Your Lucky Lotto Numbers Are:', nums)