#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 18 22:01:58 2020

@author: evanlamberson
"""

# set input miles
input_miles = 5

# convert miles to kilometers to meters
input_kilometers = input_miles / 0.62137
input_meters = 1000 * input_kilometers

# print all variables
print(
      "Miles\n", input_miles, "\nKilometers\n", input_kilometers, 
      "\nMeters\n", input_meters
      )
