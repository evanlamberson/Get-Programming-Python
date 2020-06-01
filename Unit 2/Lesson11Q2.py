#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun  1 12:40:00 2020

@author: evanlamberson
"""


### Lesson 11 Q11.2
# Write a program that asks the user’s name and then age. Use appropriate 
# variable names to store these variables. Calculate how old the user will 
# be in 25 years. For example, if the user enters Bob and 10, the program 
# should print "Hi Bob! In 25 years you will be 35!"

print("<==> FORTUNE TELLER <==>")

name = input("What... is your name? ").capitalize()
age = int(input("What... is your age in years? "))

print(name + ", according to the mystic forces, I feel that in 25 years you" 
      + " will be nearing the age of " + str(age + 25) + ".")
