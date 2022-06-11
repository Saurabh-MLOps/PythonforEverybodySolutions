fhandle = open('mbox-short.txt')
count = 0
total = 0
for line in fhandle:

    ly = line.rstrip()
    if ly.startswith('X-DSPAM-Confidence:'):
        pos = ly.find(':')       #To find the position of numbers
        num = ly[pos +1:].strip()    #Removes all except numbers
        n = float(num)
        total = total + n
        count = count + 1
        avg = total/count
        print('Average Spam Confidence:',avg)
