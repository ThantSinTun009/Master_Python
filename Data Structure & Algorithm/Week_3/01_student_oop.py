# PascalCase = UserProfile is used when we create a class
# camelCase = userProfile is used for variables and function
# snake_case = user_profile is used for variables

class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def introduce(self):
        print(f"My name is {self.name} and I am {self.age} years old.")
        # name = name (student1.name = name and student1.age = age)
        
        
student1 = Student("Alice", 20)    
student1.introduce()
        
student2 = Student("Bob", 25)
student2.introduce()

################## Exercise 1: Car Class #####################
# Attributes -> brand and speed
# method -> drive() -> "the {brand} car is driving at {speed} kw/h"

class Car:
    def __init__(self, brand, speed):
        self.brand = brand
        self.speed = speed
        
    def drive(self):
        print(f"The {self.brand} car is driving at {self.speed} kw/h")
        
car1 = Car("Toyota", 120)
car1.drive()
        
car2 = Car("BMW", 180)
car2.drive()       
        
##############################################################

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        
    def area(self):
        return self.width * self.height
    
rect1 = Rectangle(5, 3)
rect1_area = rect1.area()

print(rect1_area)

###### Exercise 2: Circle Class
# attributes -> radius
# method - area() -> 3.14 * r**2

class Circle:
    def __init__(self, radius):
        self.radius = radius
        
    def area(self):
        return f"The area of the circle: {3.14 * (self.radius ** 2)}"
    
cir1 = Circle(2)
cir1_area = cir1.area()
print(cir1_area)
        
##############################################################

        
    
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        

        
        
        
        
        