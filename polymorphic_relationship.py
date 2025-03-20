class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        
    def move(self):
        print(f"{self.brand} {self.model} is moving")
        
class Brand:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        
    def move(self):
        print(f"{self.brand} {self.model} is moving")
            
class Plane:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        
    def move(self):
        print(f"{self.brand} {self.model} is moving")
            
car1 = Car("Toyota", "Camry")
brand1 = Brand("Suzuki", "GSR")
plane1 = Plane("Boing", "747")

for x in (car1, brand1, plane1):
    x.move()
        