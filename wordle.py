import random
import time
from colorama import Fore, Back, Style
print(Style.RESET_ALL)
def slowprintnostop(string):
    for letter in string:
        print(letter, end='',flush=True)
        time.sleep(0.15)
def slowprint(string):
    for letter in string:
        print(letter, end='',flush=True)
        time.sleep(0.2)
    print(flush=False)
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
def round(number,wordlist,numberofguesses):
    print(Style.RESET_ALL)
    number=str(number)
    numberofguesses=str(numberofguesses)
    list2=['You have ',number,' guesses left']
    ' '.join(list2)
    slowprint(list2)
    Guess=[]
    Guessword=''
    while len(Guess)!=5:
        Guess=[]
        list1=['Guess #',numberofguesses]
        ' '.join(list1)
        slowprint(list1)
        Guessword=input()
        Guessword=Guessword.upper()
        for _ in Guessword:
            Guess.append(_)
        if len(Guess)!=5:
            slowprint("Sorry, your answeris not valid, it must be 5 letters long")
    if correctornot(wordlist,Guess)==True:
        slowprint('Congratulations! You win!')
        print(Style.RESET_ALL)
        return('win')
    else:
        listnumber=0
        for i in Guess:
            a=correctletter(i,wordlist[listnumber],wordlist)
            slowprintnostop(a)
            listnumber+=1
        print(flush=False)   
while True:
    word = randomword()
    word=word.upper()
    wordlist=[]
    for _ in word:
        wordlist.append(_)
    triesleft=6
    numberofguesses=1
    while triesleft!=0:
        winorlose=round(triesleft,wordlist,numberofguesses)
        triesleft-=1
        numberofguesses+=1
        if winorlose=='win':
            g=0
            while g==0:
                playagain=input('Play again?y/n')
                if playagain=='y':
                    g=1
                    triesleft=0
                elif playagain=='n':
                    quit()
                else:
                    print('That is not a valid answer, please enter either y or n')
        elif winorlose=='lose':
            print('Better luck next time! The answer was,',word)
