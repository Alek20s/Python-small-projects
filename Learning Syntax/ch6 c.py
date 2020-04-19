# -*- coding: utf-8 -*-
"""
Created on Tue Feb 11 16:36:03 2020

@author: Aleks
"""

#print(('     Hello Python').lstrip())

s= 'AAAAA'
#print (s)
#print (s.strip())
for n in range(1,30):
    print(s.center(n,' '))
print (s*4)
string = 'python in easy steps'
print ('\nCapitalized:\t', string.capitalize())
print ('\nCapitalized:\t', string.title())
print ('\nCentred:\t', string.center(30,'*'))

print('\nUppercase:\t', string.upper())
print('\nJoined:\t\t', string.join('**'))
print('nJustufied:\t', string.rjust(30,'*'))
print('\nReplaced:\t', string.replace('s','*'))









