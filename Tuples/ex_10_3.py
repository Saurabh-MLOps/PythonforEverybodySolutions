"""
Exercise 1: Revise a previous program as follows:
Read and parse the “From” lines and pull out the addresses from the line.
Count the number of messages from each person using a dictionary.

After all the data has been read,
print the person with the most commits by creating a list of (count, email) tuples from the dictionary.
Then sort the list in reverse order and print out the person who has the most commits."""






fhandle = open('mbox-short.txt')
count = dict()
for line in fhandle:
    if line.startswith('From:'):
        line = line.rstrip()
        line = line.split()
        line = line[1]
        count[line] = count.get(line,0) +1
#print(count)
lst = list()
for k,v in count.items():
    update = (v,k)
    lst.append(update)         #To reverse order from key,value to value,key
#print(lst)
lst = sorted(lst,reverse = True)     #To sort from most from least
for val,key in lst:
    print(key,val)
