# Abstraksi menyembunyikan detail implementasi dari pengguna dan hanya menampilkan fungsionalitas penting. 
# Ini dilakukan dengan membuat metode yang hanya perlu diketahui oleh pengguna.

from abc import ABC, abstractmethod

class Animal(ABC):  # Abstract class
    @abstractmethod
    def sound(self):
        pass

class Dog(Animal):
    def sound(self):
        return "Bark"

class Cat(Animal):
    def sound(self):
        return "Meow"

# Menggunakan abstract class dan derived class
dog = Dog()
cat = Cat()
print(dog.sound())  # Output: Bark
print(cat.sound())  # Output: Meow