# Encapsulation and Class Basics
class Car:
    def model(self):
        return "Camry"
    def __init__(self, fuel_level):
        self.fuel_level = fuel_level
    def add_fuel(self, amount):
        self.fuel_level += amount
    def get_current_fuel_level(self):
        return self.fuel_level
    def year(self):
        return "2023"
    def color(self):
        return "red"
    def description(self):
        return f"This is a {self.color()} {self.year()} {self.model()} with {self.get_current_fuel_level()}  gallons of fuel left."

my_car = Car(input("enter the fuel level: "))
print(my_car.description())


# Inheritance and Polymorphism
def animal_sound(animal):
    print(animal.speak())
class Dog():
    def speak(self):
        return "woof"
class Duck():
    def speak(self):
        return "quack"
my_dog = Dog()
my_duck = Duck()
animal_sound(my_duck)

