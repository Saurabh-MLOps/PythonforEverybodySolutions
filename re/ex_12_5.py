"""
Now we can use regular expressions to redo an exercise from earlier in the book where we were interested in the time of day of each mail message. We looked for lines of the form:

From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
"""

import re
fhand = open('mbox-short.txt')
for line in fhand:
    line = line.rstrip()
    x = re.findall('^From .* ([0-9][0-9]):',line)      #The translation of this regular expression is that we are looking for lines that start with From (note the space), followed by any number of characters (.*), followed by a space, followed by two digits [0-9][0-9], followed by a colon character.
    if len(x) > 0:
        print(x)
