# 🚧 OOP Concepts

# Class definition
class Animal:
    """Base class for all animals"""
    
    # Class variable (shared by all instances)
    kingdom = "Animalia"
    
    # Constructor (initializer)
    def __init__(self, name, age):
        # Instance variables
        self.name = name
        self.age = age
        self._health = 100  # Protected attribute (convention)
        self.__id = hash(self)  # Private attribute (name mangling)
    
    # Instance method
    def speak(self):
        return f"{self.name} makes a sound"
    
    def get_info(self):
        return f"{self.name} is {self.age} years old"
    
    # Getter for private attribute
    def get_id(self):
        return self.__id
    
    # Class method
    @classmethod
    def get_kingdom(cls):
        return cls.kingdom
    
    # Static method
    @staticmethod
    def is_animal(thing):
        return isinstance(thing, Animal)


# Inheritance
class Dog(Animal):
    def __init__(self, name, age, breed):
        # Call parent constructor
        super().__init__(name, age)
        self.breed = breed
    
    # Method overriding (polymorphism)
    def speak(self):
        return f"{self.name} barks: Woof! Woof!"
    
    def fetch(self):
        return f"{self.name} fetches the ball"


class Cat(Animal):
    def __init__(self, name, age, color):
        super().__init__(name, age)
        self.color = color
    
    def speak(self):
        return f"{self.name} meows: Meow!"
    
    def scratch(self):
        return f"{self.name} scratches the furniture"


# Multiple inheritance
class Bird(Animal):
    def speak(self):
        return f"{self.name} chirps: Tweet tweet!"
    
    def fly(self):
        return f"{self.name} flies through the sky"


class Pet(Dog, Cat):  # Multiple inheritance
    def __init__(self, name, age, breed, color):
        # MRO (Method Resolution Order) determines which parent's init is called
        Dog.__init__(self, name, age, breed)
        self.color = color


# Encapsulation with properties
class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.__balance = balance  # Private attribute
    
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            return f"Deposited ${amount}. New balance: ${self.__balance}"
        return "Invalid amount"
    
    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            return f"Withdrew ${amount}. New balance: ${self.__balance}"
        return "Insufficient funds or invalid amount"
    
    # Property decorator (getter)
    @property
    def balance(self):
        return self.__balance
    
    # Setter with validation
    @balance.setter
    def balance(self, amount):
        if amount >= 0:
            self.__balance = amount
        else:
            raise ValueError("Balance cannot be negative")


# Abstraction using ABC (Abstract Base Class)
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
    
    @abstractmethod
    def perimeter(self):
        pass
    
    def description(self):
        return f"This is a shape with area {self.area()} and perimeter {self.perimeter()}"


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height
    
    def perimeter(self):
        return 2 * (self.width + self.height)


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return 3.14159 * self.radius ** 2
    
    def perimeter(self):
        return 2 * 3.14159 * self.radius


# Polymorphism demonstration
def make_animal_speak(animal):
    print(animal.speak())


# Testing OOP concepts
if __name__ == "__main__":
    # Creating objects
    generic_animal = Animal("Generic", 5)
    dog = Dog("Buddy", 3, "Golden Retriever")
    cat = Cat("Whiskers", 2, "Orange")
    
    # Using methods
    print(generic_animal.get_info())
    print(dog.get_info())
    print(dog.speak())
    print(dog.fetch())
    print(cat.speak())
    print(cat.scratch())
    
    # Polymorphism
    print("\nPolymorphism:")
    animals = [dog, cat, Bird("Tweety", 1)]
    for animal in animals:
        print(animal.speak())
    
    # Encapsulation with BankAccount
    print("\nEncapsulation:")
    account = BankAccount("Alice", 1000)
    print(account.deposit(500))
    print(account.withdraw(200))
    print(f"Balance via getter: ${account.balance}")
    
    # Abstract classes
    print("\nAbstraction:")
    rect = Rectangle(5, 3)
    circle = Circle(4)
    print(f"Rectangle area: {rect.area()}")
    print(f"Circle area: {circle.area():.2f}")
    
    # Magic methods (dunder methods)
    class Vector:
        def __init__(self, x, y):
            self.x = x
            self.y = y
        
        def __add__(self, other):
            return Vector(self.x + other.x, self.y + other.y)
        
        def __str__(self):
            return f"Vector({self.x}, {self.y})"
        
        def __repr__(self):
            return f"Vector({self.x}, {self.y})"
    
    v1 = Vector(2, 3)
    v2 = Vector(4, 5)
    v3 = v1 + v2
    print(f"\nMagic methods: {v1} + {v2} = {v3}")
