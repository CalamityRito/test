import os
def getcontent():
    try:
        i=input('Enter the file name:')
        with open(i,'r') as h: 
            content=h.read()
        h.close()
        return(content)
    except:
        print('Invalid answer')
def addcontent():
    try:
        i=input('Enter the file name:')
        j=input('Enter the content:')
        with open(i,'a') as h:
            h.write(j)
        h.close()
    except:
        print('Invalid answer')
def newname():
    i=input('Enter the file name:')
    j=input('Enter the new name:')
    os.rename(i,j)
def lines():
    i=input('Enter the file name:')
    h=open (i)
    count=[]
    for line in h:
        count.append(line)
    h.close()
    return(len(count))
def exists():
    i=input('Enter the file name:')
    try:
        open(i)
        return(True)
    except:
        return(True)
print(getcontent())
addcontent()
newname()
print(lines())
print(exists())