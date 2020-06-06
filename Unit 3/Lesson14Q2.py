# -*- coding: utf-8 -*-
"""
Created on Tue Jun  2 13:48:24 2020

@author: Evan
"""
### Lesson 14 Q14.2
# Write a program that reads in a string from the user. If the string contains
# at least one of every vowel (a, e, i, o, u), print "You have all the vowels!"
# Additionally, if the string starts with the letter a and ends in the letter
# z, print "And it's sort of alphabetical!"

# Get string from user
string = input("Hey! Give me a string. ").lower()

# Boolean expression to count vowels
# My original solution:
#vowel_count = (string.count("a") > 0 and string.count("e") > 0 
               #and string.count("i") > 0 and string.count("o") > 0 
               #and string.count("u") > 0)

# The solution out of the book:
vowel_count = ("a" in string and "e" in string and "i" in string and "o" in
               string and "u" in string)

if vowel_count == True:
    print("You have all the vowels!")
    if (string[0] == "a") and (string[-1] == "z"):
        print("And it's sort of alphabetical!")

