import random
from colorama import Fore, Back, Style
print(Style.RESET_ALL)
def randomword():
    listofwords=['ANGEL','ANGLE','BEGIN','BEING','BINGE','STOPS','SPOTS','POSTS','TRAPS','STRAP','PARTS','CARES','CARTS','SPACE','SCALE','LACES']
    word=random.choice(listofwords)
    return(word)
def correctornot(word, guess):
    if word==guess:
        return(True)
    else:
        return(False)
def correctletter(letter,letter_2,word):
    if letter==letter_2:
        return(Fore.GREEN + letter)
    elif letter in word:
        return(Fore.YELLOW + letter)
    else:
        return(Fore.RED + letter)

while True:
    word = randomword()
    word = word.upper()
    wordlist=[]
    for _ in word:
        wordlist.append(_)
    print('You have six guesses left')
    Guess1=[]
    Guess1word=''
    while len(Guess1)!=5:
        Guess1=[]
        Guess1word=input("What is your first guess?")
        Guess1word=Guess1word.upper()
        for _ in Guess1word:
            Guess1.append(_)
        if len(Guess1)!=5:
            print("Sorry, your answeris not valid, it must be 5 letters long")
    number=0
    if correctornot(wordlist,Guess1)==True:
        print('Congratulations! You win!')
    else:
        for i in Guess1:
            print(correctletter(i,wordlist[number],wordlist))