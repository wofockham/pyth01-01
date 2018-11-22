# lr.py - a Python line reader / filter
# sample usage: python3 lr.py ulysses.txt

# "somestring"[::-1] - extended slice syntax - reverses a string

import fileinput

for line in fileinput.input():
    print(line, end="")
