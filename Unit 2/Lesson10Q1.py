#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun  1 11:49:04 2020

@author: evanlamberson
"""


### Lesson 10 Q10.1
# Write a program that initializes the string word = "echo", the empty tuple
# t = (), and the integer count = 3. Then, write a sequence of commands by 
# using the commands you learned in this lesson to make t = ("echo", "echo", 
# "echo", "cho", "cho", "cho", "ho", "ho", "ho", "o", "o", "o") and print it.
# The original word is added to the end of the tuple, and then the original 
# word without the first letter is added to the tuple, and so on. Each 
# substring of the original word gets repeated count number of times.

## Method 1

# initialize vars
word = "echo"
t = ()
count = 3

#add word to tuple, then shorten word 
t += (word,) * count
word = word[1:]
t += (word,) * count
word = word[1:]
t += (word,) * count
word = word[1:]
t += (word,) * count


print("Method 1:", t)

## Method 2

# initialize vars
word = "echo"
t = ()
count = 3

# while loop to clean up Method 1 
i = 1
length = len(word)
while i <= length:
    t += ((word,) * count)
    word = word[1:]
    i += 1

print("Method 2:", t)
