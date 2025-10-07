# Class: A blueprint for creating objects 
# Object: An instance of a class
# Medthods: Function inside a class
class Dog:
    def __init__(self,name):
        self.name = name # attribute of class dog which is one 
    def get_name(self):
        return self.name
    def set_name(self,name):
        self.name = name
    

d = Dog("Tim")
d.bark()
print(type(d))
