# -*- coding: utf-8 -*-
"""
Created on Thu Feb  6 18:11:28 2020

@author: Aleks
"""

import sys, keyword
print ('Python Version', sys.version)
print ('Python Interpreter Location', sys.executable)
print ('Python Module Search Path:')
for dir in sys.path:
    print (dir)
print ('Python Keywords:')
for word in keyword.kwlist:
    print (word)