# -*- coding: utf-8 -*-
"""
Created on Wed Feb  5 17:47:43 2020

@author: Aleks
"""

chars= ['Alpha', 'Beta', 'Gamma', 'Delta', 'Epsilon']
def display (elem):
    assert type(elem) is int, 'Argument must be Integer!'
    print ('List Element', elem, '=', chars[elem])

elem = 4
display (elem)
elem = elem/2
display (elem)