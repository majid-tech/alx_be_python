# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def print_message(self):
#         return f'Hello! your name is {self.name}, and age is {self.age}.'

#     def __del__(self):
#         return f'Good bye'

# person = Person("Majid", 34)

# print(person.print_message())

# class Book:
#     def __init__(self, title, author, pages):
#         self.title = title
#         self.author = author
#         self.pages = pages

#     def __str__(self):
#         return f'Book title: {self.title} | Author: {self.author} | Pages: {self.pages}'

# book1 = Book("Usul Hadith", "Dr. Bilal Philips", 163)

# print(book1)

# Inheritance
# class Shape:
#     def __init__(self, l, b):
#         self.l = l
#         self.b = b

#     def calculate_area(self):
#         return self.l * self.b
    
# class Rectangle(Shape):
#     def calculate_area(self):
#         return super().calculate_area()
    
# rec = Rectangle(10, 10)
# print(rec.calculate_area())

# Multiple inheritance 
# class Bird:
#     @property
#     def fly(self):
#         print("flying")

# class Mammal:
#     @property
#     def run(self):
#         print("run")

# class Bat(Bird, Mammal):
#     pass

# bat = Bat()
# bat.fly
# bat.run

# class method...
# class Book:
#     total_books = 0

#     def __init__(self, name):
#         self.name = name
#         Book.total_books += 1

#     @classmethod
#     def display_total_books(cls):
#         print(f'Total books created: {cls.total_books}')

# bk1 = Book("Hadeeth")
# bk2 = Book("Fiqh")
# bk3 = Book("Tawhid")

# Book.display_total_books()

# static method...
# class Calculator:
#     @staticmethod
#     def add(a, b):
#         return a + b
    
#     @staticmethod
#     def multiply(a, b):
#         return a * b
    
# print(Calculator.add(4, 5))
# print(Calculator.multiply(4, 5))

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def create_child(cls):
        age = 0
        return age
    
print(Person.create_child())