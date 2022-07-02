import re
fhand = open('mbox-short.txt')
for line in fhand:
    line = line.rstrip()
    x = re.findall('^X-.*: ([0-9.]+)',line)
    if len(x) > 0:
        print(x)
    
