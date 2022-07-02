"""
Exercise 2: Write a program to look for lines of the form:

New Revision: 39772
Extract the number from each of the lines using a regular expression and the findall() method.
Compute the average of the numbers and print out the average as an integer."""

import re
counts = 0
lst = list()
fhand = open('mbox-short.txt')
for line in fhand:
    line = line.rstrip()
    x = re.findall('^New .*: ([0-9]+)',line)

    if len(x)>0:
        counts+=1
        for number in x:
            number = float(number)
            lst.append(number)
avg = sum(lst)/counts
print(avg)
