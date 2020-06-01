#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun  1 14:41:19 2020

@author: evanlamberson
"""


### Lesson 13 Quick Check 13.7
# How many chocolate bars should I buy?

# Set price and hungriness
price = float(input("We finally made it to the grocery store! Oh man! They "
                    "have chocolate bars! I wonder how much they cost? I can "
                    "see the price tag, but I forgot my glasses at home and "
                    "it's too blurry. Could you tell me what the price is? "))
hungry = input("Alright well I guess we'll buy some if "
               "you're hungry. You are hungry right? (yes or no): ")

# Determines how many chocolate bars to buy if hungry
if hungry == "yes":
    if price < 1:
        print("Only $" + str(price) + "?! Let's buy them all!")
        bars = 100
    if 1 <= price <= 5:
        print("That's pretty steep... let's buy ten.")
        bars = 10
    if price > 5:
        print("Holy crap! $" + str(price) + "?! We can just share one.")

if hungry == "no":
    print("Yeah, we better just stick to the list.")

if bars > 10:
    print("Cashier: Pretty hungry today, aren't we?")