# -*- coding: utf-8 -*-
"""
Created on Sun Feb  2 18:51:55 2020

@author: Aleks
"""

basket= ['Apple', 'Apple', 'Bun', 'Cola']
crate = ['Egg', 'Fig', 'Grape']
print ('Basket List:', basket )
print ('Basket Elements:', len (basket))
print (basket.count('Apple'))
#basket.append(4)
basket.extend(crate)
basket.insert(1, 'mellon')
basket.pop(1)
number = basket.count('Apple')
print (basket)
basket.sort()
basket.reverse()
print (basket)
print (number)
