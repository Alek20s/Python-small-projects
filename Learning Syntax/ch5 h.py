# -*- coding: utf-8 -*-
"""
Created on Mon Feb 10 18:34:48 2020

@author: Aleks
"""

from re import*

pattern = \
complile('(^|\s)[-a-z0-9_.]+@([-a-z0-9]+\.)+[a-z]{2,6}(\s|S)')

def get_address():
    address = input ('enter')
    is_valid = pattern.match (address)
    if is_valid:
        print ('valid', is_valid.group())
    else:
        print('invalid')
get_address()