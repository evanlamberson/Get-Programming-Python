#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun  1 14:30:23 2020

@author: evanlamberson
"""


### Lesson 13 Quick Check 13.4
# 1
word = input("Please input a word. ")
print("Here's your word:", word)
if word.count(" ") > 0:
    print("You didn't follow the instructions!")

# 2
num1 = int(input("Hey you! Gimme a number! "))
num2 = int(input("Hey now! Gimme another! "))
sum1 = num1 + num2
print("Here's sum-thing for ya trouble:", sum1)
if sum1 < 0:
    print("Hey now! That's a negative sum!")