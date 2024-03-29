######################################################################
# Author: Samantha Schweinsberg     TODO: Change this to your name
# Username: schweinsbergs           TODO: Change this to your username
#
# Assignment: A01
#
# Purpose: A program that returns your Chinese Zodiac animal given a
# birth year between 1988 and 1999. Also prints your friend's animal,
# and your compatibility with that friend's animal.
######################################################################
# Acknowledgements:
#   Original Author: Dr. Scott Heggen
######################################################################

# Remember to read the detailed notes about each task in the A01 document.

######################################################################
# (Required) Task 1
# TODO Ask user for their birth year

year = int(input("Enter your year of birth to find your Chinese Zodiac!"))
if year == 1999:
    print("You're a rabbit!")
elif year == 2000:
    print("You're a dragon!")
elif year == 2001:
    print("You're a snake!")
elif year == 2002:
    print("You're a horse!")
elif year == 2003:
    print("You're a goat!")
elif year == 2004:
    print("You're a monkey!")
elif year == 2005:
    print("You're a rooster!")
elif year == 2006:
    print("You're a dog!")
elif year == 2007:
    print("You're a pig!")
elif year == 2008:
    print("You're a rat!")
elif year == 2009:
    print("You're an ox!")
elif year == 2010:
    print("You're a tiger!")

# TODO Check the year using if conditionals, and print the correct animal for that year.
# See the a01_pets.py for examples


######################################################################
# (Required) Task 2
# TODO Ask the user for their friend's birth year
name = input("What's your friend's name?")
year = int(input("What's your friend's birth year?"))
if year == 1999:
    print( name + " is a rabbit!")
elif year == 2000:
    print( name + " is a dragon!")
elif year == 2001:
    print( name + " is a snake!")
elif year == 2002:
    print( name + " is a horse!")
elif year == 2003:
    print( name + " is a goat!")
elif year == 2004:
    print( name + " is a monkey!")
elif year == 2005:
    print( name + " is a rooster!")
elif year == 2006:
    print( name + " is a dog!")
elif year == 2007:
    print( name + " is a pig!")
elif year == 2008:
    print( name + " is a rat!")
elif year == 2009:
    print( name + " is a ox!")
elif year == 2010:
    print( name + " is a rabbit!")


# TODO Similar to above, check your friend's year using if conditionals, and print the correct animal for that year


######################################################################
# (Optional) Task 3
# TODO Check for compatibility between your birth year and your friend's birth year
# NOTE: You can always assume the first input is your birth year (i.e., 1982 for me).
# This way, you are not writing a ton of code to consider every possibility.
# In other words, only do one row of the sample compatibility table.


# TODO print if you are a strong match, no match, or in between
