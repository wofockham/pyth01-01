# lr.py - a Python line reader / filter
# sample usage: python3 lr.py ulysses.txt

# "somestring"[::-1] - extended slice syntax - reverses a string

import fileinput
import re

pattern = re.compile("\.") # escaping: \. - the \ turns off the special meaning of "." (alternatively [.])

for line in fileinput.input():
    # Print the line if it contains/matches the regular expression pattern
    if pattern.search(line):
        print(line, end="")
