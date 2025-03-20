class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    
    def move(self):
        print("RkB")
        
class Car(Vehicle):
    pass

class Brand(Vehicle):
    def move(self):
        print("Saikot")
        
class Plane(Vehicle):
    def move(self):
        print('Robeen')

car1 = Car("Toyota", "Camry")
brand1 = Brand("Suzuki", "GSR")
plane1 = Plane("Boing", "747")

for x in (car1, brand1, plane1):
    print(x.model)
    print(x.brand)
    x.move()    
        
    