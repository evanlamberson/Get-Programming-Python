# -*- coding: utf-8 -*-
"""
Created on Tue Jun  2 13:12:02 2020

@author: Evan
"""
### Lesson 13 Q13.5
# Find the absolute value of a user's given integer

num = int(input("What would you like to find the absolute value of? "))

if num < 0:
    num *= -1

print("The absolute value is: " + str(num) + ".")
    

