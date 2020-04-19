# -*- coding: utf-8 -*-
"""
Created on Sun Feb  2 19:22:31 2020

@author: Aleks
"""

basket= ['Apple', 'Bun', 'Cola']
crate = ['Egg', 'Fig', 'Grape']
 
print('Basket List:', basket)
print ('Basket Elements:', len(basket))

basket.append('Damson')
print ('Appended', basket)
basket.pop()
print ('Last Item Removed:', basket )
basket.extend(crate)
print ('Extended',basket)
del basket[1]
print ('Item removed', basket)

del basket[1:3]
print ('Slice removed', basket)



