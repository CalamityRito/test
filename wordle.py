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
    listofwords=['ANGEL','ANGLE','BEGIN','BEING','BINGE','STOPS','SPOTS','POSTS','TRAPS','STRAP','PARTS','CARES','CARTS','SPACE','SCALE','LACES','GREEN']
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
def roundwith4(number,wordlist,wordlist2,wordlist3,wordlist4,numberofguesses):
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
    
    
    listnumber=0
    for i in Guess:
        a=correctletter(i,wordlist[listnumber],wordlist)
        slowprintnostop(a)
        listnumber+=1
    print(flush=False)
    listnumber=0
    for i in Guess:
        a=correctletter(i,wordlist2[listnumber],wordlist2)
        slowprintnostop(a)
        listnumber+=1
    print(flush=False)
    listnumber=0
    for i in Guess:
        a=correctletter(i,wordlist3[listnumber],wordlist3)
        slowprintnostop(a)
        listnumber+=1
    print(flush=False)
    listnumber=0
    for i in Guess:
        a=correctletter(i,wordlist4[listnumber],wordlist4)
        slowprintnostop(a)
        listnumber+=1
    print(flush=False)
    if correctornot(wordlist,Guess)==True:
        return('win 1')
    elif correctornot(wordlist2,Guess)==True:
        return('win 2')
    elif correctornot(wordlist3,Guess)==True:
        return('win3')
    elif correctornot(wordlist4,Guess)==True:
        return('win 4')
    else:
        return('')
def roundwith3(number,wordlist,wordlist2,wordlist3,numberofguesses):
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
    
    
    listnumber=0
    for i in Guess:
        a=correctletter(i,wordlist[listnumber],wordlist)
        slowprintnostop(a)
        listnumber+=1
    print(flush=False)
    listnumber=0
    for i in Guess:
        a=correctletter(i,wordlist2[listnumber],wordlist2)
        slowprintnostop(a)
        listnumber+=1
    print(flush=False)
    listnumber=0
    for i in Guess:
        a=correctletter(i,wordlist3[listnumber],wordlist3)
        slowprintnostop(a)
        listnumber+=1
    print(flush=False)
    if correctornot(wordlist,Guess)==True:
        return('win 1')
    elif correctornot(wordlist2,Guess)==True:
        return('win 2')
    elif correctornot(wordlist3,Guess)==True:
        return('win3')
    else:
        return('')
def roundwith2(number,wordlist,wordlist2,numberofguesses):
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
    
    
    listnumber=0
    for i in Guess:
        a=correctletter(i,wordlist[listnumber],wordlist)
        slowprintnostop(a)
        listnumber+=1
    print(flush=False)
    listnumber=0
    for i in Guess:
        a=correctletter(i,wordlist2[listnumber],wordlist2)
        slowprintnostop(a)
        listnumber+=1
    print(flush=False)
    listnumber=0
    if correctornot(wordlist,Guess)==True:
        return('win 1')
    elif correctornot(wordlist2,Guess)==True:
        return('win 2')
    return('')
def roundwith1(number,wordlist,numberofguesses):
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
    
    
    listnumber=0
    for i in Guess:
        a=correctletter(i,wordlist[listnumber],wordlist)
        slowprintnostop(a)
        listnumber+=1
    print(flush=False)
    listnumber=0
    if correctornot(wordlist,Guess)==True:
        return('win')
    else:
        return('')
while True:  
    word = randomword()
    word=word.upper()
    wordlist=[]
    word2 = randomword()
    word2=word2.upper()
    wordlist2=[]
    word3 = randomword()
    word3=word3.upper()
    wordlist3=[]
    word4 = randomword()
    word4=word4.upper()
    wordlist4=[]
    for _ in word4:
        wordlist4.append(_)
    for _ in word3:
        wordlist3.append(_)
    for _ in word2:
        wordlist2.append(_)
    for _ in word:
        wordlist.append(_)
    triesleft=9
    numberofguesses=1
    a1=False
    a2=False
    a3=False
    a4=False
    notsolved=[]
    while triesleft!=0:
        if a1==False:
            notsolved.append('')
        if a2==False:
            notsolved.append('')
        if a3==False:
            notsolved.append('')
        if a4==False:
            notsolved.append('')
        if len(notsolved)==4:
            winorlose=roundwith4(triesleft,wordlist,wordlist2,wordlist3,wordlist4,numberofguesses)
            if winorlose=='win 1':
                a1=True
            elif winorlose=='win 2':
                a2=True
            elif winorlose=='win 3':
                a3=True
            elif winorlose=='win 4':
                a4=True
        elif len(notsolved)==3:
            if a1==True:
                winorlose=roundwith3(triesleft,wordlist2,wordlist3,wordlist4,numberofguesses)
                if winorlose=='win 1':
                    a2=True
                if winorlose=='win 2':
                    a3=True
                if winorlose=='win 3':
                    a4=True
            elif a2==True:
                winorlose=roundwith3(triesleft,wordlist,wordlist3,wordlist4,numberofguesses)
                if winorlose=='win 1':
                    a1=True
                if winorlose=='win 2':
                    a3=True
                if winorlose=='win 3':
                    a4=True
            elif a3==True:
                winorlose=roundwith3(triesleft,wordlist,wordlist2,wordlist4,numberofguesses)
                if winorlose=='win 1':
                    a1=True
                if winorlose=='win 2':
                    a2=True
                if winorlose=='win 3':
                    a4=True
            elif a4==True:
                winorlose=roundwith3(triesleft,wordlist,wordlist2,wordlist3,numberofguesses)
                if winorlose=='win 1':
                    a1=True
                if winorlose=='win 2':
                    a2=True
                if winorlose=='win 3':
                    a3=True
        elif len(notsolved)==2:
            if a1 == True and a2 == True:
                winorlose=roundwith2(triesleft,wordlist3,wordlist4,numberofguesses) 
                if winorlose=='win 1':
                    a3=True
                if winorlose=='win 2':
                    a4=True
            elif a1 == True and a3 == True:
                winorlose=roundwith2(triesleft,wordlist2,wordlist4,numberofguesses)
                if winorlose=='win 1':
                    a2=True
                if winorlose=='win 2':
                    a4=True
            elif a1 == True and a4 == True:
                winorlose=roundwith2(triesleft,wordlist2,wordlist3,numberofguesses)
                if winorlose=='win 1':
                    a2=True
                elif winorlose=='win 2':
                    a3=True
            elif a2 == True and a3 == True:
                winorlose=roundwith2(triesleft,wordlist,wordlist4,numberofguesses)
                if winorlose=='win 1':
                    a1=True
                elif winorlose=='win 2':
                    a4=True
            elif a2 == True and a4 == True:
                winorlose=roundwith2(triesleft,wordlist,wordlist3,numberofguesses)
                if winorlose=='win 1':
                    a1=True
                elif winorlose=='win 2':
                    a3=True
            elif a3 == True and a4 == True:
                winorlose=roundwith2(triesleft,wordlist,wordlist2,numberofguesses)
                if winorlose=='win 1':
                    a1=True
                elif winorlose=='win 2':
                    a2=True
        elif len(notsolved)==1:
            if a1==False:
                winorlose=roundwith1(triesleft,wordlist,numberofguesses)
            elif a2==False:
                winorlose=roundwith1(triesleft,wordlist2,numberofguesses)
            elif a3==False:
                winorlose=roundwith1(triesleft,wordlist3,numberofguesses)
            elif a4== False:
                winorlose=roundwith1(triesleft,wordlist4,numberofguesses)
        while len(notsolved)!=0:
            notsolved.pop()
        triesleft=triesleft-1
        numberofguesses=numberofguesses+1
        if winorlose=='win':
            slowprint('Congratulations! You win!')
            g=0
            while g==0:
                print(Style.RESET_ALL)
                playagain=input('Play again?y/n')
                if playagain=='y':
                    g=1
                    triesleft=0
                    numberofguesses=0
                elif playagain=='n':
                    quit()
                else:
                    print('That is not a valid answer, please enter either y or n')
        elif winorlose=='lose':
            print('Better luck next time! The answer was,',word)
            g=0
            while g==0:
                playagain=input('Play again?y/n')
                if playagain=='y':
                    g=1
                    triesleft=0
                    numberofguesses=1
                elif playagain=='n':
                    quit()
                else:
                    print('That is not a valid answer, please enter either y or n')