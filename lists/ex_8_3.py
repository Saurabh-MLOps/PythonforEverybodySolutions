file = input("Enter the file name:")
fhandle = open(file,'r')
lst = list()
for line in fhandle:
    word = line.rstrip().split()
    for element in word:
        if element in lst:
            continue
        else:
            lst.append(element)
lst.sort()
print(lst)
