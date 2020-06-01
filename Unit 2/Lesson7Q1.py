#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun  1 10:58:39 2020

@author: evanlamberson
"""
###Lesson 7 Q7.1
# Write one or more commands that uses the string "Guten Morgen" to get TEN. 
# There is more than one way to do this.
input_string = "Guten Morgen"

# Method 1
output_string = input_string[2:5].upper()
print("Method 1:", output_string)

# Method 2
output_string = input_string[2:5].swapcase()
print("Method 2:", output_string)

# Method 3
output_string = input_string[2] + input_string[10:]
output_string = output_string.upper() # swapcase() would work here too
print("Method 3:", output_string)