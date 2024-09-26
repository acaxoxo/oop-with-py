# Polimorfisme memungkinkan metode yang sama untuk bekerja dengan cara yang berbeda tergantung pada objek yang memanggilnya.

class Bird:
    def fly(self):
        return "Bird can fly"

class Penguin(Bird):
    def fly(self):
        return "Penguins can't fly"

def make_fly(bird):
    print(bird.fly())

# Menggunakan polymorphism
sparrow = Bird()
penguin = Penguin()

make_fly(sparrow)  # Output: Bird can fly
make_fly(penguin)  # Output: Penguins can't fly