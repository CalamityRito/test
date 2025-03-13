# Excercise 1

def chop(list):
    i=len(list)
    i-=1
    list.pop(i)
    list.pop(0)
    return(None)
list1=['a','b','c','d','e']
chop(list1)
print(list1)

# Excercises 2 & 3 

try:
    fhand = open('mbox-short.txt')
    count = 0
    for line in fhand:
        words = line.split()
        if len(words) != 0 and words[0] == 'From':
            print(words[2])
except:
    print('Error')

# Excercise 4

list1=[]
list2=[]
with open('romeo.txt') as h:
    for line in h:
        a=line.split()
        for item in a:
            if item not in list1:
                list1.append(item)
    h.close()
list1.sort()
for item in list1:
    print(item)

# Excercise 5
k=[]
with open('mbox-short.txt') as h:
    for line in h:
        if line.startswith('From:'):
            k=line.split()
            print(k[1])
