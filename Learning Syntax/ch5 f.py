# -*- coding: utf-8 -*-
"""
Created on Sun Feb  9 21:29:30 2020

@author: Aleks
"""

from datetime import datetime
#today = datetime()

print ('Today Is:', today)
#stoday = str(today)
#for attr in today: #['year', 'month','day', 'hour', 'minute', 'second', 'milisecond']:    
#    print(attr, ':\t', getattr(today,attr))

day = today.strftime('%A')
month = today.strftime('%B')
print ('Date', day, month, today.day)