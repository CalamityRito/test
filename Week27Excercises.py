#Excercises 1&3:
#Basic Class Definition and Adding Attributes
class Animal:
    def __init__(self,att):
        self.att=att
    def make_sound(self):
        print('woof woof')
tim=Animal('three two one')
tim.make_sound()
#Excercises 2&3:
#Inheritance and Using Attributes
class Dog(Animal):
    def make_sound(self):
        print(self.att)
john=Dog('master')
john.make_sound()
#Excercise 4:
#Multiple Subclasses
class Cat(Animal):
    def make_sound(self):
        print(self.att,'sucks')
mary=Cat('Mary')
mary.make_sound()