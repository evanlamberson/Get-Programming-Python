#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun  1 11:22:51 2020

@author: evanlamberson
"""


### Lesson 8 Q8.1
#   Write a program that initializes a string with the value "Eat Work Play 
# Sleep repeat". Then, use the string manipulation commands you’ve learned so 
# far to get the string "working playing".

input = "Eat Work Play Sleep repeat"

## Method 1
a:int # buffer variable to store index locations

# Getting "working"
a = input.find("Work")
working = input[a:a + len("Work")].lower() + "ing"

# Getting "playing"
a = input.find("Play")
playing = input[a:a + len("Play")].lower() + "ing"

output = working + " " + playing
print("Method 1:", output)


## Method 2
output = input.replace("Eat Work Play Sleep repeat", "working playing")
print("Method 2:", output)