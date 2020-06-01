#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun  1 13:40:13 2020

@author: evanlamberson
"""

### Lesson 12: Unit 2 Capstone Project
## Name Mashup
# When two names are entered in the format FIRSTNAME LASTNAME, user receives
# two new names created by fusing the two different names together.
# Ex. Dave Gibson and Roger Wright -> Dager Gibght and Rove Wrison

# Get both input names in format FIRST LAST
print("Welcome to the Name Masher!")
name1 = input("Enter one full name (FIRST LAST): ")
name2 = input("Enter another full name (FIRST LAST): ")

# Split full names into first and last names
i = name1.find(" ")
(name1_first, name1_last) = (name1[0:i], name1[i + 1:])
i = name2.find(" ")
(name2_first, name2_last) = (name2[0:i], name2[i + 1:])

# Split names into halves
i_name1_first = int(len(name1_first) / 2)
i_name2_first = int(len(name2_first) / 2)
i_name1_last = int(len(name1_last) / 2)
i_name2_last = int(len(name2_last) / 2)

l_name1_first = name1_first[0:i_name1_first]
r_name1_first = name1_first[i_name1_first:]
l_name2_first = name2_first[0:i_name2_first]
r_name2_first = name2_first[i_name2_first:]

l_name1_last = name1_last[0:i_name1_last]
r_name1_last = name1_last[i_name1_last:]
l_name2_last = name2_last[0:i_name2_last]
r_name2_last = name2_last[i_name2_last:]

# Combine halves into new names
new_name1 = (
    (l_name1_first + r_name2_first).capitalize() + " " +
    (l_name1_last + r_name2_last).capitalize()
    )

new_name2 = (
    (l_name2_first + r_name1_first).capitalize() + " " + 
    (l_name2_last + r_name1_last).capitalize()
    )

# Print new names
print("All done! Pick your favorite!")
print(new_name1)
print(new_name2)



