#Excercise 1:
#Basic Class Definition
class Animal:
    def __init__(self):
        pass
    def make_sound(self):
        print('woof woof')
tim=Animal()
tim.make_sound()
#Excercise 2:
#Inheritance
class Dog(Animal):
    def __init__(self):
        pass
    def make_sound(self):
        print('bark bark')
john=Dog()
john.make_sound()
