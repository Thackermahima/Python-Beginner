# A class is like a blueprint for creating objects. An object has properties and methods(functions) associated with it. Almost everything in Python is an object

class User: 
    def __init__(self, name, age):
        self.name = name 
        self.age = age
    def greeting(self):
     return f'My name is {self.name} and I am {self.age}'
 
brad = User('brand',77)
print(brad.name)



print(brad.greeting())


#Extend the class 

class Customer(User): 
     def __init__(self, name, age):
        self.name = name 
        self.age = age
        self.balance = 0 
    
     def set(self, balance): 
        self.balance = balance
        
        Jene = Customer('brand',77)
        Jene.set(5)
