#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 18 16:52:59 2020

@author: evanlamberson
"""
### Input variable ###
minutes_to_convert = 789

### Generate hours_part ###
hours_decimal = minutes_to_convert/60
hours_part = int(hours_decimal)

### Generate minutes_part ###
## There are two possible solutions here. I will show both.
## Solution 1
#minutes_part = round((hours_decimal -  hours_part) * 60)
# Gets decimal remainder of minutes_to_convert and multiplies it by 60 to find total minutes, 
# then rounds it to closest integer.
## Solution 2
minutes_part = minutes_to_convert % 60
# Gets the whole number remainder of the hours conversion directly

### Generates output ###
print("Hours")
print(hours_part)
print("Minutes")
print(minutes_part)
s


