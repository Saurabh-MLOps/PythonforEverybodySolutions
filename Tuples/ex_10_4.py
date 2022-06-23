"""
Exercise 2: This program counts the distribution of the hour of the day for each of the messages.
You can pull the hour from the “From” line by finding the time string and then splitting that string into parts using the colon character.
Once you have accumulated the counts for each hour, print out the counts, one per line, sorted by hour as shown below."""

#Python timeofday.py program:

fhand = open('mbox-short.txt')
count = dict()
for line in fhand:
    if line.startswith('From '):
        line = line.rstrip()
        line = line.split()
        line = line[5]
        line = line.split(':')
        line = line[0]
        #print(line)
        count[line] = count.get(line,0) + 1
#print(count)
lst = list()
for key,value in count.items():
    update = (key,value)
    lst.append(update)
    lst = sorted(lst)
for k,v in lst:                                 #To present the data in a vertical line
    print(k,v)
