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
u=input('Enter file name:')
average=0
count2=0
try:
    with open(u) as v:
        for line2 in v:
            if len(line2)==0: continue
            line2=line2.strip()
            j=re.findall('^New Revision: ([0-9]+)',line2)
            if len(j)>0:
                count2+=1
                t=int(j[0])
                average+=t
except:
    print("ERROR")
print(average/count2)
