# -*- coding: utf-8 -*-
"""
Created on Mon Feb  3 12:54:31 2020

@author: Aleks
"""

chars = ['A', 'B', 'C']
fruit = ('Apple', 'Banana', 'Cherry')
weight =[3,5,9]
dict = {'name': 'Alex', 'ref': 'Python', 'sys': 'Win'}


print ('n\Elements:\t', end = '')
for item in chars:
    print (item, end ='')
    
print ('\nEnumerated:\t', end ='')
for item in enumerate(chars):
    print (item, end = '   ')
print ('n\Paired:')
for key, value in dict.items():
    print (key, '=', value)

print ('\nZipped:\t', end = '')
for item in zip (chars, fruit, weight):
    print (item, end = ' ')
        
        





