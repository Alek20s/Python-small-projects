# -*- coding: utf-8 -*-
"""
Created on Mon Feb  3 18:43:57 2020

@author: Aleks
"""
def echo(user, lang,sys):
    print ('User:', user, 'Language:', lang, 'Platform:', sys)
echo('Mike', 'Python', 'Windwos')
echo (lang= 'python', sys = 'MacOS', user = 'Anne')


def mirror(user = 'Carole', lang = 'Python'):
    print('\nUser:', user, 'Language', lang)
mirror()
mirror(lang = 'Java')
mirror(user= 'Tony')
mirror('Sussan', 'C++')



