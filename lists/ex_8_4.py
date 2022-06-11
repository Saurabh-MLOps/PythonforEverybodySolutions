fname = input('Enter the file name:')
try:
    fhandle = open(fname)
except:
    print('Error: Not a valid file name')

print(fname)
count = 0
for line in fhandle:
    word = line.rstrip().split()
    if len(word) > 0 and word[0] == 'From':
        count = count + 1
        print(word[1])
        continue
print('There were',count,'lines in the file with From as the first word')
