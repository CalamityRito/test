import re

# Fruit Text for exercises 1-6
fruit_text = "I have an apple, a banana, and another apple."
# Exercise 1: Using re.search
# Find the first occurrence of the word "apple" in the fruit_text
if bool(re.search('apple',fruit_text))==True:
    print('There is the word "apple" in: "',fruit_text,'"')
# Exercise 2: Using re.findall
# Find all occurrences of the word "apple" in the fruit_text
y=re.findall('apple',fruit_text)
print(len(y))
# Exercise 3: Using re.search with a more complex pattern
# Find the first occurrence of a word that starts with 'b' and ends with 'a' in the fruit_text
if bool(re.search(r' b[a-zA-Z]*a[,. ]',fruit_text))==True:
    print('There is a word that starts with b and ends with a in: "',fruit_text,'"')
# Exercise 4: Using re.findall with a more complex pattern
# Find all words that start with 'a' and end with 'e' in the fruit_text
x=re.findall(r' a[a-zA-Z]*e[,. ]',fruit_text)
print(x)
# Exercise 5: Using re.search with groups
# Find the first occurrence of a word that starts with 'a' and capture the word in the fruit_text
f=fruit_text.split()
for item in f:
    if bool(re.search(r'^a.+$',item))==True:
        print(item)
        break
# Exercise 6: Using re.findall with groups
# Find all words that start with 'a' and capture the words in the fruit_text
for item in f:
    if bool(re.search(r'^a.+$',item))==True:
        print(item)
# Phone Text for exercises 7-8
phone_text = "My phone number is 123-456-7890."
# Exercise 7: Using re.search with a digit pattern
# Find the first occurrence of a digit in the phone_text
if bool(re.search(r'[0-9\-]',phone_text))==True:
    print('There is a digit in: "',phone_text,'"')
# Exercise 8: Using re.findall with a digit pattern
# Find all occurrences of digits in the phone_text
n=phone_text.split()
for item in n:
    y=re.findall(r'[0-9]',item)
    for i in y:
        print(i)
# Mary text for exercises 9-10
mary_text = "My name is Mary and I live in Miami."
# Exercise 9: Using re.search with a word boundary pattern
# Find the first occurrence of a word that starts with 'M' and ends with 'y' in mary_text
m=mary_text.split()
for item in m:
    if bool (re.search(r'^M.*y$',item))==True:
        print('There is a word starting with "M" and ending with "y" in "',mary_text,'"')
        break
# Exercise 10: Using re.findall with a word boundary pattern
# Find all words that start with 'M' and end with 'y' in mary_text
for item in m:
    o=re.findall(r'M.*y',item)
    for item in o:
        print(item)
# Email text for exercises 11-12
email_text = "Please contact us at support@example.com or sales@example.com."
# Exercise 11: Using re.search with an email pattern
# Find the first occurrence of an email address in the email_text
list2=email_text.split()
for item in list2:
    if bool(re.search(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.]+\.[a-zA-Z][a-zA-Z]+$',item))==True:
        print(item)
# Exercise 12: Using re.findall with an email pattern
# Find all occurrences of email addresses in the email_text
h=re.findall(r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.]+\.[a-zA-Z][a-zA-Z]+',email_text)
for item in h:
    print(item)