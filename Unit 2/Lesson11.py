#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun  1 12:08:21 2020

@author: evanlamberson
"""


### Quick Check Lesson 11.2 

sweet = "cookies"
savory = "pickles"
num = 100
print(num, savory, "and", num, sweet)
print(savory[1].upper() + " choose the " + sweet.upper() + "!")

### Quick Check Lesson 11.3

input("Tell me a secret? ")
input("What's your favorite color? ")
input("Enter any of the following: '#, $, %, &, or *'. ")

### Quick Check Lesson 11.4

fav_song = input("What's your favorite song? ")
print((fav_song + "\n") * 3)

first_name = input("What's your favorite celebrity's first name? ")
last_name = input("What's their last name? ")
print(first_name + "\n" + last_name)

### Quick Check Lesson 11.5

num = int(input("Enter a number to find the square of: "))
print(float(num * num))