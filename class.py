class Hello:
    x = 5
    
p = Hello()
print(p.x)

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def myFunction(self):
        print("Hello my name is " + self.name)
        
p1 = Person("John", 36)
print(p1.name)
print(p1.age)
p1.myFunction()