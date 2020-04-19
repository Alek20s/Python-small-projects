# -*- coding: utf-8 -*-
"""
Created on Sun Feb  2 19:40:02 2020

@author: Aleks
"""

colors_set= {'Red', 'Green', 'Red', 'Blue', 'Red'}
print (colors_set)
zoo = ('Kangaroo', 'Leopard', 'Moose')
print ('Tuple:', zoo, '\tLength:', len(zoo))
print (type(zoo))

bag ={'Red', 'Green', 'Blue'}
bag.add('Yellow')
print ('\Set:', bag, 'tLength', len(bag))
t = type(bag)
print (t)

print ('ls Green In Bag Set?:', 'Green' in bag)
print ('ls Orange In Bag Set?:', 'Orange' in bag)

box = {'Red', 'Purple', 'Yellow'}
print ('\nSet:', box, '\t\tLength', len(box))
print ('Common To Both Sets:', bag.intersection(box))






