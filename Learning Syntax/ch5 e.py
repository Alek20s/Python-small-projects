# -*- coding: utf-8 -*-
"""
Created on Sun Feb  9 21:02:08 2020

@author: Aleks
"""
from decimal import*
item= (0.70)
rate = 1.05

tax = item*rate
total = item +tax

print ('Item:\t', '%.2f'% item)
print ('Tax:\t', '%.2f'% tax)
print ('Total:\t', '%.2f'% total)

item =Decimal(0.70)

print ('Item:\t', '%.20f'% item)
print ('Tax:\t', '%.20f'% tax)
print ('Total:\t', '%.20f'% total)
