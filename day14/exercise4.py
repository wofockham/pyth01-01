# lr.py - a Python line reader / filter
# sample usage: python3 lr.py ulysses.txt

# "somestring"[::-1] - extended slice syntax - reverses a string

import fileinput
import re

# Make a program that prints each line that has a word that is capitalized but not ALL capitalized. Does it match Fred but neither fred nor FRED?

pattern = re.compile("[A-Z][a-z]")

for line in fileinput.input():
    # Print the line if it contains/matches the regular expression pattern
    if pattern.search(line):
        print(line, end="")
