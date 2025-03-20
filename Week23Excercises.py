a=input('Enter file name:')
d=dict()
d2=dict()
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
list2=[]
try:
    with open(a) as h:
        for line in h:
            if line.startswith('From '):
                i=line.split()
                p=i[5].split(':')
                d2[p[0]]=d2.get(p[0],0)+1
        for item in d2:
            list2.append((item,d2[item]))
        list2.sort()
        for t,j in list2:
            print(t,j)
except:
    print('nope')
d3=dict()
mostfrequent=['',0]
try:
    with open(a) as h:
        for line in h:
            for _ in line:
                d3[_]=d3.get(_,0)+1
    for item in d3:
        item=str(item)
        if item.isalpha():
            if int(d3[item])>mostfrequent[1]:
                mostfrequent=[item,d3[item]]
    for item in mostfrequent:
        print(item)
except:
    print('Get your OWN name!')