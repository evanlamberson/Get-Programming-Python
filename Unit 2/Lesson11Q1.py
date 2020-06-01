#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun  1 12:20:29 2020

@author: evanlamberson
"""


### Lesson 11 Q11.1
# Write a program that asks the user for two numbers. Store these numbers in
# variables b and e. The program calculates and prints the power b^e with an 
# appropriate message.

print("Calculate whole number exponents!")
b = int(input("What is the base? "))
e = int(input("What is the exponent? "))
print(str(b) + "^" + str(e) + " = " + str(b ** e))