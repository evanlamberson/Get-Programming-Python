# -*- coding: utf-8 -*-
"""
Created on Tue Jun  2 13:16:59 2020

@author: Evan
"""
### Lesson 14 Q14.1
# Write a program that reads in two numbers from the user. The program should
# print the relation between the two numbers, which will be one of the
# following: "numbers are equal", "first number is less than the second
# number", "first number is greater than the second number."

# Gets two numbers from user
num_1 = int(input("Hey! I'm the number comparer.\nNow give me a number! "))
num_2 = int(input("Now give me another! "))

# Compares the two numbers
if num_1 == num_2:
    print("Those numbers are equal.")
elif num_1 < num_2:
    print("The first number you gave me is less than the second number.")
elif num_1 > num_2:
    print("The first number you gave me is greater than the second number.")

