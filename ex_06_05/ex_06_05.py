str = 'X-DSPAM-Confidence: 0.8475'
ipos = str.find(':')
nstr = str[19:len(str)]
value = float(nstr)
