fhandle = open('mbox-short.txt')
for letter in fhandle:
    if letter.startswith('X-DSPAM-Confidence:'):
        print(letter)
