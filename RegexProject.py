import re
def validate_name(name):
    return bool(re.search(r'[a-zA-Z][a-z]+ *[a-zA-Z]*[a-z]*',name))
def validate_email(email):
    return bool(re.search(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.]+\.[a-zA-Z][a-zA-Z]+',email))
def validate_phone_number(number):
    if len(re.findall('[0-9]',number))==10: 
        return bool(re.search(r'^[0-9\-]+$',number))
print(validate_name('Example Name'))
print(validate_email('exampleemail%.700987@mastermail.com'))
print(validate_phone_number('720-720-7207'))
