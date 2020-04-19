# -*- coding: utf-8 -*-
"""
Created on Mon Feb 24 21:53:33 2020

@author: Aleks
"""

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("John", 36)

print(p1.name)
print(p1.age) 