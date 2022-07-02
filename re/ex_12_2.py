import re
fhand = open('mbox-short.txt')
for line in fhand:
    line = line.rstrip()
    if re.search('^X-.*: [0-9.]+',line):
        print(line)
