# -*- coding: utf-8 -*-
"""
Created on Wed Feb  5 17:24:33 2020

@author: Aleks
"""

title = 'Python in Easy Steps'
try:
    print ('titel')
except NameError as msg:
        print (msg)
        
day = 32
try:
    if day >31:
        raise ValueError('Invalid Day Number')
except ValueError as msg:
        print ('The program found An', msg)
finally:
    print ('But Today is Beautiful Anyway.')

