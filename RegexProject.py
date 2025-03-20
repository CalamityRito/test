import re
def validate_name(name):
    return bool(re.search(r'[a-zA-Z][a-z]+ *[a-zA-Z]*[a-z]*',name))
def validate_email(email):
    return bool(re.search(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.]+\.[a-zA-Z][a-zA-Z]+',email))
def validate_phone_number(number):
    if len(re.findall('[0-9]',number))==10: 
        return bool(re.search(r'^[0-9\-]+$',number))
def format_name(name):
    list1=[]
    returner=''
    for _ in name:
        h=bool(re.search(r'[a-zA-Z ]',_))
        if h==True:
            list1.append(_)
    for item in list1:
        returner=returner+item
    return(returner)
def format_phone_number(number):
    list1=[]
    list2=[]
    returner=''
    for _ in number:
        h=bool(re.search(r'[0-9\-]',_))
        if h==True:
            list1.append(_)
    for item in list1:
        p=bool(re.search(r'[0-9]',item))
        if p==True:
            list2.append('/')
        else:
            list2.append(item)
    for item in list2:
        returner=returner+item
    return(returner)
print(validate_name('Example Name'))
print(validate_email('exampleemail%.700987@mastermail.com'))
print(validate_phone_number('720-720-7207'))
print(format_name('Z-e,* ^Ba(ld/w"i$n'))
print(format_phone_number('&7*2&0^%-7()20$#-7:;;207"""'))