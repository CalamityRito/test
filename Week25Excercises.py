import re
y=input('Enter a regular expression:')
count=0
with open('mbox-short.txt') as h:
    for line in h:
        if len(line)==0: continue
        line=line.strip()
        x=re.findall(y,line)
        if len(x) > 0:
            count+=1
print('mbox-short.txt had',count,'lines that matched',y)