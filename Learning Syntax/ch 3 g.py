# -*- coding: utf-8 -*-
"""
Created on Mon Feb  3 12:04:41 2020

@author: Aleks
"""

a,b = 1, 2
while b < 1000:
    print (a,b)
    a,b = b, a+b
    
i=1
while i<4:
    print ('n\Outer Loop Interactions:', i)
    i +=1
    j=1
    while j<6:
        print ('\tInner Loop Interaction:', j)
        j +=1
        
        
        
        