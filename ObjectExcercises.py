#Excercise 1: 
#creating a class called person and adding an "introduce" function

class person(object):
    def __init__(self,name,age,email):
        self.name=name
        self.age=age
        self.email=email
    def introduce(self):
        print('This is', self.name,", who's age is",self.age,', and email is,',self.email)



#Excercise 2
#creating a class called book and adding a "summary" function 

class book(object):
    def __init__(self,title,author,pages):
        self.title=title
        self.author=author
        self.pages=pages
    def summarize(self,summary):
        self.summary=summary
        print('This book is called',self.title,'and can be summarizeed as follows:')
        print(self.summary)

#Excercise 3:
#creating a class called library and giving it multiple functions

class library(object):
    def __init__(self,name,books,members):
        self.name=name
        self.books=books
        self.members=members
    def addmember(self,member):
        self.members.append(member)
    def addbook(self,book):
        self.books.append(book)
    def libraryinfo(self):
        h=''
        g=''
        for item in self.members:
            h=h+item
            h=h+'. '
        for item in self.books:
            g=g+item
            g=g+'. '
        print('This is the',self.name,'\nWe have the books:',g,'\nOur members are:',h)


#Excercise 4:
#demonstrating each class, and its functions

john=person('John',25,'Johnthemaster@gmail.com')
john.introduce()

harrypotter=book('Harry Potter','J. K. Rowling',309)
harrypotter.summarize('A classic tale of three kids, Harry, Hermione, and\nRon, and their adventures at Hogwarts school\nof witchcraft and wizardry')

utahcountylibrary=library('Utah County Library',['Maze Runner','Hunger Games','Harry Potter','Lord of the Rings','Dune'],['John','Anna','Tom'])
utahcountylibrary.addmember('Hank')
utahcountylibrary.addbook('Anne of green gables')
utahcountylibrary.libraryinfo()