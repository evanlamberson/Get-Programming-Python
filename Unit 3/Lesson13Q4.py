# -*- coding: utf-8 -*-
"""
Created on Tue Jun  2 13:08:33 2020

@author: Evan
"""
### Lesson 13 Q13.4

secret_num = 18
user_num = int(input("Guess my number!\nWhat do you guess? "))

if user_num < secret_num:
    print("Too low!")

if user_num > secret_num:
    print("Too High!")

if user_num == secret_num:
    print("You got it!")
