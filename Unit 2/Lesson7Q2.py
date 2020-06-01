#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun  1 11:07:27 2020

@author: evanlamberson
"""


### Lesson 7 Q7.2
# Write one or more commands that uses the string "RaceTrack" to get Ace.

input_string = "RaceTrack"

# Method 1
output_string = input_string[1:4].capitalize()
print("Method 1:", output_string)

# Method 2
output_string = input_string[1].upper() + input_string[-2] + input_string[3]
print("Method 2:", output_string)

# Method 3
output_string = (input_string[-3] + input_string[2:4].upper()).swapcase()
print("Method 3:", output_string)