# Dont need to rewrite them, only thing specific to dog and cat is the speak method 

class Pet:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    
    def show(self):
        print(f"I am {self.name} and I am {self.age} years old")


class Cat(Pet):
    def __init__(self,name,age,color):
        super().__init__(name,age)
        self.color = color 
        
    def speak(self):
        print("Meow")
    
    def show(self):
        print(f"I am {self.name} and I am {self.color}")

class Dog(Pet):
    def __init__(self,name,age,breed):
        super().__init__(name,age)
        self.breed = breed

    def speak(self):
        print("Bark")




