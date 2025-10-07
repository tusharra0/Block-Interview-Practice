# Class: A blueprint for creating objects 
# Object: An instance of a class
# Medthods: Function inside a class
class Dog:
    def __init__(self,name):
        self.name = name # attribute of class dog which is one 
        print(name)

    def add_one(self,x):
        return x+1
    
    def bark(self):
        print("bark")

d = Dog("Tim")
d.bark()
print(type(d))
