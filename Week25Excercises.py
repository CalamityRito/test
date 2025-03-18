import re
y=input('Enter a regular expression:')
with open('mbox-short.txt') as h:
    y=y+'.+$'
    f=h.read()
    print(re.findall(y,f))