a=input('Enter file name:')
d=dict()
list1=[]
mostcommon=('',0)
try:
    with open(a) as h:
        for line in h:
            if len(line)<2: continue
            if line.startswith('From'):
                j=line.split()
                d[j[1]]=d.get(j[1],0)+1/2
    for i in d:
        d[i]=int(d.get(i))
        list1.append((i,d[i]))
    for item in list1:
        if item[1]>mostcommon[1]:
            mostcommon=item
    for item in mostcommon:
        print(item)
except:
    print('Error')