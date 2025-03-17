j=input('Enter file name:')
d=dict()
try:
    with open(j) as h:
        for line in h:
            if not line.startswith('From'): continue
            u=line.split()
            d[u[1]]=d.get(u[1],0)+1
        for v in d:
            d[v]=int(d.get(v)/2)
    print(d)
except:
    print('Error, invalid file name.')   
list1=[]
list2=[]
for k in d:
    list2=[k,d[k]]
    list1.append(list2)
highest=['',0]
for i in list1:
    if i[1]>highest[1]:
        highest=i
print(highest[0],highest[1])
d2=dict()
try:
    with open(j) as y:
        for line in y:
            if not line.startswith('From'): continue
            m=line.split('@')
            r=m[1].split()
            d2[r[0]]=d2.get(r[0],0)+1
    for item in d2:
        d2[item]=int(d2.get(item)/2)
    print(d2)
except:
    print('Error')