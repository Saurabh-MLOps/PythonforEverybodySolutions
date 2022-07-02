import re
fhand = open('mbox-short.txt')
for line in fhand:
    line = line.rstrip()
    x = re.findall('[a-zA-Z0-9]\S*@\S*',line)
    if len(x)>0:
        print(x)
