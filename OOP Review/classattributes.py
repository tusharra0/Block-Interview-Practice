# class attributes are specific to class not to instance and object of that class 

class Person:
    number_of_people = 0 

    def __init__(self,name):
        self.name = name
        Person.add_person()
        
    

    @classmethod # act on class it self , doesnt have acess to any instance hence cls not self 
    def number_of_people_(cls):
        return cls.number_of_people()

    @classmethod
    def add_person(cls):
        cls.number_of_people+=1
    
    
p1 = Person("tim")
p2 = Person("jill")
Person.number_of_people = 8 
print(p1.number_of_people)
print(Person.number_of_people)