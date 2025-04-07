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
class Contacts:
    def __init__(self,name,phone_number,email):
        self.name=name
        self.phone_number=phone_number
        self.email=email
    def str(self):
        print('Contact Name:',self.name,'\nContact Phone Number:',self.phone_number,'\nContact Email:',self.email)
class Contactbook:
    def __init__(self,contacts):
        self.contacts=list(contacts)
    def addcontact(self,contact):
        self.contacts.append(contact)
    def deletecontact(self,contact):
        self.contacts.remove(contact)
    def searchcontact(self,contact):
        if contact in self.contacts:
            return(True)
        else:
            return(False)
    def displaycontacts(self):
        for item in self.contacts:
            print(item)
phone=Contactbook([])
while True:

    h=input('Contact Book Menu: \n1. Add Contact\n2. Delete Contact\n3. Search Contact\n4. Display Contacts\n5. exit\n')
    if h=='1':
        j=input('What is the name of the contact you would like to add?')
        phone.addcontact(j)
        input(j+' added!')
    elif h=='2':
        j=input('What is the name of the contact you would like to delete?')
        try:
            phone.deletecontact(j)
            input(j+' deleted!')
        except:
            print('Error. Invalid answer.')
    elif h=='3':
        j=input('What is the name of the contact you would like to search for?')
        if bool(phone.searchcontact(j))==True:
            input(j+' is in the contact book')
        else:
            input(j+' is not in the contact book')
    elif h=='4':
        phone.displaycontacts()
        input()
    elif h=='5':
        print('See you again soon!')
        quit()
    else:
        input('Error. that is not a valid answer. Please input a number from 1 to 5')


