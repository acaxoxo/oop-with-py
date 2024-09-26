# Pewarisan adalah konsep di mana sebuah class bisa mewarisi atribut dan metode dari class lain. 
# Class yang diwarisi disebut parent class (atau base class), dan class yang mewarisi disebut child class (atau derived class).

class Vehicle:
    def __init__(self, brand):
        self.brand = brand

    def drive(self):
        return "Driving"

class Car(Vehicle):  # Car mewarisi Vehicle
    def __init__(self, brand, model):
        super().__init__(brand)  # Memanggil konstruktor dari Vehicle
        self.model = model

    def honk(self):
        return "Honking"

# Menggunakan inheritance
car = Car("Toyota", "Corolla")
print(car.brand)  # Output: Toyota
print(car.drive())  # Output: Driving
print(car.honk())   # Output: Honking