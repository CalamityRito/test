import random
import time
from colorama import Fore, Style
try:
    with open('highestwinstreak.txt','r')as h:
        h.close()
except:
    with open('highestwinstreak.txt','w') as h:
        h.close()
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
def fastprint(string):
    for letter in string:
        print(letter,end='',flush=True)
        time.sleep(0.075)
    print(flush=False)
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
def roundwith4(number,wordlist,wordlist2,wordlist3,wordlist4,numberofguesses,listofwords):
    print(Style.RESET_ALL)
    number=str(number)
    numberofguesses=str(numberofguesses)
    list2=['You have ',number,' guesses left']
    ' '.join(list2)
    slowprint(list2)
    Guess=[]
    Guessword=''
    while len(Guess)!=5 or Guessword not in listofwords:
        Guess=[]
        list1=['Guess #',numberofguesses]
        ' '.join(list1)
        slowprint(list1)
        Guessword=input()
        Guessword=Guessword.upper()
        for _ in Guessword:
            Guess.append(_)
        if len(Guess)!=5 or Guessword not in listofwords:
            fastprint("Sorry, your answer is not valid, it must be 5 letters long, and must be a real word.\nIf it is a real word, I am sorry, but it is not in the list of five letter words we have")

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
def roundwith3(number,wordlist,wordlist2,wordlist3,numberofguesses,listofwords):
    print(Style.RESET_ALL)
    number=str(number)
    numberofguesses=str(numberofguesses)
    list2=['You have ',number,' guesses left']
    ' '.join(list2)
    slowprint(list2)
    Guess=[]
    Guessword=''
    while len(Guess)!=5 or Guessword not in listofwords:
        Guess=[]
        list1=['Guess #',numberofguesses]
        ' '.join(list1)
        slowprint(list1)
        Guessword=input()
        Guessword=Guessword.upper()
        for _ in Guessword:
            Guess.append(_)
        if len(Guess)!=5 or Guessword not in listofwords:
            fastprint("Sorry, your answer is not valid, it must be 5 letters long, and be a real word\nIf it is a real word, I am sorry, but it is not in the list of five letter words we have")
    
    
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
def roundwith2(number,wordlist,wordlist2,numberofguesses,listofwords):
    print(Style.RESET_ALL)
    number=str(number)
    numberofguesses=str(numberofguesses)
    list2=['You have ',number,' guesses left']
    ' '.join(list2)
    slowprint(list2)
    Guess=[]
    Guessword=''
    while len(Guess)!=5 or Guessword not in listofwords:
        Guess=[]
        list1=['Guess #',numberofguesses]
        ' '.join(list1)
        slowprint(list1)
        Guessword=input()
        Guessword=Guessword.upper()
        for _ in Guessword:
            Guess.append(_)
        if len(Guess)!=5 or Guessword not in listofwords:
            fastprint("Sorry, your answer is not valid, it must be 5 letters long, and must be a real word\nIf it is a real word, I am sorry, but it is not in the list of five letter words we have")
    
    
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
def roundwith1(number,wordlist,numberofguesses,listofwords):
    print(Style.RESET_ALL)
    number=str(number)
    numberofguesses=str(numberofguesses)
    list2=['You have ',number,' guesses left']
    ' '.join(list2)
    slowprint(list2)
    Guess=[]
    Guessword=''
    while len(Guess)!=5 or Guessword not in listofwords:
        Guess=[]
        list1=['Guess #',numberofguesses]
        ' '.join(list1)
        slowprint(list1)
        Guessword=input()
        Guessword=Guessword.upper()
        for _ in Guessword:
            Guess.append(_)
        if len(Guess)!=5 or Guessword not in listofwords:
            fastprint("Sorry, your answer is not valid, it must be 5 letters long,and must be a real word\nIf it is a real word, I am sorry, but it is not in the list of five letter words we have")
    
    
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
    listofwords=['ANGEL','ANGLE','BEGIN','BEING','BINGE','STOPS','SPOTS','POSTS','TRAPS','STRAP','PARTS','CARES','CARTS','SPACE','SCALE','LACES','GREEN']
    h=open('fiveLetterWords.txt')
    for line in h:
        line=line.upper()
        linelist=[]
        for _ in line:
            linelist.append(_)
        linelist.pop()
        line=''.join(linelist)
        listofwords.append(line)
    word=random.choice(listofwords)
    word=word.upper()
    wordlist=[]
    word2=random.choice(listofwords)
    word2=word2.upper()
    wordlist2=[]
    word3=random.choice(listofwords)
    word3=word3.upper()
    wordlist3=[]
    word4=random.choice(listofwords)
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
    triesleft=20
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
            winorlose=roundwith4(triesleft,wordlist,wordlist2,wordlist3,wordlist4,numberofguesses,listofwords)
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
                winorlose=roundwith3(triesleft,wordlist2,wordlist3,wordlist4,numberofguesses,listofwords)
                if winorlose=='win 1':
                    a2=True
                if winorlose=='win 2':
                    a3=True
                if winorlose=='win 3':
                    a4=True
            elif a2==True:
                winorlose=roundwith3(triesleft,wordlist,wordlist3,wordlist4,numberofguesses,listofwords)
                if winorlose=='win 1':
                    a1=True
                if winorlose=='win 2':
                    a3=True
                if winorlose=='win 3':
                    a4=True
            elif a3==True:
                winorlose=roundwith3(triesleft,wordlist,wordlist2,wordlist4,numberofguesses,listofwords)
                if winorlose=='win 1':
                    a1=True
                if winorlose=='win 2':
                    a2=True
                if winorlose=='win 3':
                    a4=True
            elif a4==True:
                winorlose=roundwith3(triesleft,wordlist,wordlist2,wordlist3,numberofguesses,listofwords)
                if winorlose=='win 1':
                    a1=True
                if winorlose=='win 2':
                    a2=True
                if winorlose=='win 3':
                    a3=True
        elif len(notsolved)==2:
            if a1 == True and a2 == True:
                winorlose=roundwith2(triesleft,wordlist3,wordlist4,numberofguesses,listofwords) 
                if winorlose=='win 1':
                    a3=True
                if winorlose=='win 2':
                    a4=True
            elif a1 == True and a3 == True:
                winorlose=roundwith2(triesleft,wordlist2,wordlist4,numberofguesses,listofwords)
                if winorlose=='win 1':
                    a2=True
                if winorlose=='win 2':
                    a4=True
            elif a1 == True and a4 == True:
                winorlose=roundwith2(triesleft,wordlist2,wordlist3,numberofguesses,listofwords)
                if winorlose=='win 1':
                    a2=True
                elif winorlose=='win 2':
                    a3=True
            elif a2 == True and a3 == True:
                winorlose=roundwith2(triesleft,wordlist,wordlist4,numberofguesses,listofwords)
                if winorlose=='win 1':
                    a1=True
                elif winorlose=='win 2':
                    a4=True
            elif a2 == True and a4 == True:
                winorlose=roundwith2(triesleft,wordlist,wordlist3,numberofguesses,listofwords)
                if winorlose=='win 1':
                    a1=True
                elif winorlose=='win 2':
                    a3=True
            elif a3 == True and a4 == True:
                winorlose=roundwith2(triesleft,wordlist,wordlist2,numberofguesses,listofwords)
                if winorlose=='win 1':
                    a1=True
                elif winorlose=='win 2':
                    a2=True
        elif len(notsolved)==1:
            if a1==False:
                winorlose=roundwith1(triesleft,wordlist,numberofguesses,listofwords)
            elif a2==False:
                winorlose=roundwith1(triesleft,wordlist2,numberofguesses,listofwords)
            elif a3==False:
                winorlose=roundwith1(triesleft,wordlist3,numberofguesses,listofwords)
            elif a4== False:
                winorlose=roundwith1(triesleft,wordlist4,numberofguesses,listofwords)
        while len(notsolved)!=0:
            notsolved.pop()
        triesleft=triesleft-1
        numberofguesses=numberofguesses+1
        if winorlose=='win':
            slowprint('Congratulations! You win!')
            with open('winstreak.txt','a') as h:
                h.write('win')
                h.close()
            with open('winstreak.txt','r') as h:
                number=0
                for line in h:
                    if line=='win':
                        number+=1
                    elif line=='lose':
                        number==0
                h.close()
            with open('highestwinstreak.txt','r') as h:
                j=int(h)
                h.close()
            with open('highestwinstreak.txt','w') as h:
                if j<number:
                    h.write(number)
                    j=number
                h.close()
            streak=("Your current win streak is:",number)
            highest=("Your all-time highest winstreak is;",j)
            slowprint(streak)
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
            with open('winstreak.txt','a') as h:
                h.write('lose')
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