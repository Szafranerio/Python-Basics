#Class 
class Animal:
    def walk(self):
        print('Walking')
        
class Dog(Animal):
    def __init__(self, name, age): 
        self.name = name
        self.age = age
    
    def bark(self):
        print('woof!')
        
roger = Dog('Roger', 5)

print(roger.name)
print(roger.age)
print(roger.walk())

#Modules 
#Break the code into some files so it is more clean :)

import dog #Import everything, later define

dog.bark()

from dog import walk #This is importing what we want
walk()

