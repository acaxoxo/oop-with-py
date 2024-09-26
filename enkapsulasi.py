# Enkapsulasi adalah konsep di mana data (atribut) dan metode (fungsi) disatukan ke dalam satu unit yang disebut class. 
# Penggunaan akses level, seperti private dan public, melindungi data dari akses langsung.

class Person:
    def __init__(self, name, age):
        self.name = name       # Public attribute
        self.__age = age       # Private attribute (using double underscore)

    def get_age(self):         # Public method
        return self.__age      # Accessing private attribute via a method
    
    def set_age(self, age):    # Public method
        if age > 0:
            self.__age = age

# Menggunakan class
person = Person("Aca", 19)
print(person.name)             # Output: Alice
print(person.get_age())        # Output: 25

person.set_age(30)
print(person.get_age())        # Output: 30