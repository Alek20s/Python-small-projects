# -*- coding: utf-8 -*-
"""
Created on Tue Feb 11 15:46:58 2020

@author: Aleks
"""

snack = '{} and {}'.format('Burger', 'Fires')
print('\nReplaced:', snack)

snack = '{1} and {0}'.format('Burger', 'Fires')
print('Replaced:', snack)

new = '{}, {} and {}'.format('Burger', 'Fires', 'Cherry')
print (new)

new = '{2}, {1} and {0}'.format('Burger', 'Fires', 'Cherry')
print (new)

snack ='%s and %s' % ('Milk', 'Cookies')
print ('\nSubstituted:', snack)

