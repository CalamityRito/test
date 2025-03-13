#Excercise 1

d=dict()
list1=[]
count=0
with open('FiveLetterWords.txt') as h:
    for line in h:
        list1=line.split()
        for item in list1:
            d[item]=d.get(item,0)+1
print(d)

# Excercise 2

d2=dict()
with open('mbox-short.txt') as h:
    for line in h:
        list1=line.split()
        if len(list1)>2 and line.startswith('From'):
            g=list1[2]
            d2[g]=d2.get(g,0)+1
print(d2)