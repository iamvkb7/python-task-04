🐍 Python Internship Program — Task 4
Object-Oriented Programming (OOP)
Python Topic Concepts Type Status Paradigm


A comprehensive deep-dive into Object-Oriented Programming in Python — covering classes, objects, encapsulation, inheritance, polymorphism, abstraction, and access modifiers through real-world practical programs.

📋 Table of Contents
Overview
Learning Objectives
Theory Notes
Classes and Objects
Constructors
Instance Variables and Methods
Class Variables
Encapsulation
Inheritance
Polymorphism
Abstraction
Method Overriding
super() Function
Access Modifiers
Programs Implemented
File Structure
Key Concepts Covered
Conclusion
Author
🌟 Overview
This repository contains Python programs created as part of Task 4 of the Python Internship Program. The objective of this task is to develop a thorough understanding of Object-Oriented Programming (OOP) — one of the most fundamental and widely-used programming paradigms in modern software development.

Object-Oriented Programming organises software design around data (objects) rather than functions and logic. An object can be defined as a data field that has unique attributes and behaviour. OOP enables developers to model real-world entities in code, making programs more intuitive, scalable, and maintainable.

This task covers all four core pillars of OOP — Encapsulation, Inheritance, Polymorphism, and Abstraction — along with supporting concepts like constructors, class vs instance variables, method overriding, the super() function, and access modifiers. Each concept is implemented through practical, real-world programs.

🎯 Learning Objectives
#	Objective
1	Understand the concept of classes and objects in Python
2	Learn to use constructors (__init__) to initialise objects
3	Differentiate between instance variables and class variables
4	Understand and implement instance methods
5	Apply Encapsulation to protect data using access modifiers
6	Implement Inheritance to promote code reuse across classes
7	Understand and apply Polymorphism for flexible method behaviour
8	Use Abstraction to hide implementation details via abstract classes
9	Override methods in child classes using Method Overriding
10	Use the super() function to access parent class members
11	Understand public, protected, and private access modifiers
12	Build real-world systems using OOP principles
📚 Theory Notes
1. Classes and Objects
A class is a blueprint or template for creating objects. It defines a set of attributes (data) and methods (behaviour) that the objects created from it will have.

An object is an instance of a class — a concrete entity created from the blueprint, with its own unique state.

Syntax

class ClassName:
    # class body
    pass
Example

class Dog:
    def bark(self):
        print("Woof!")

# Creating an object
my_dog = Dog()
my_dog.bark()   # Output: Woof!
Key Points

Term	Description
Class	Blueprint / Template for objects
Object	An instance of a class
Attribute	Data stored inside an object
Method	Function defined inside a class
Advantages of Classes and Objects

🏗️ Models real-world entities naturally in code
🔄 Enables creation of multiple independent objects from one blueprint
📦 Groups related data and behaviour together
🔧 Simplifies large program design and maintenance
2. Constructors (__init__)
A constructor is a special method that is automatically called when an object is created. In Python, the constructor is defined using __init__. It is used to initialise the attributes of an object at the time of creation.

Syntax

class ClassName:
    def __init__(self, parameters):
        self.attribute = value
Example

class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

s1 = Student("vimal", 21)
print(s1.name)   # Output: vimal
print(s1.age)    # Output: 21
Key Points

Feature	Detail
Method name	Always __init__
Called automatically	Yes — on object creation
Purpose	Initialise object attributes
self parameter	Refers to the current object instance
💡 Note: self is not a keyword in Python — it is a convention. However, it must always be the first parameter of any instance method, including __init__.

3. Instance Variables and Methods
Instance variables are variables that are unique to each object. They are defined inside the __init__ method using self and hold data specific to each instance.

Instance methods are functions defined inside a class that operate on instance variables. They always take self as their first parameter.

Example

class Car:
    def __init__(self, brand, speed):
        self.brand = brand     # instance variable
        self.speed = speed     # instance variable

    def display_info(self):    # instance method
        print(f"Brand: {self.brand}, Speed: {self.speed} km/h")

car1 = Car("Toyota", 180)
car2 = Car("BMW", 240)

car1.display_info()   # Output: Brand: Toyota, Speed: 180 km/h
car2.display_info()   # Output: Brand: BMW, Speed: 240 km/h
Key Points

Feature	Detail
Defined with	self.variable_name inside __init__
Scope	Unique to each object instance
Accessed via	object.variable_name
Instance method	Takes self as first parameter
4. Class Variables
A class variable is a variable that is shared across all instances of a class. It is defined inside the class body but outside any method. All objects of the class share the same class variable unless individually overridden.

Example

class Employee:
    company_name = "Tech Corp"    # class variable

    def __init__(self, name):
        self.name = name          # instance variable

e1 = Employee("vimal")
e2 = Employee("Rahul")

print(e1.company_name)   # Output: Tech Corp
print(e2.company_name)   # Output: Tech Corp

Employee.company_name = "New Corp"
print(e1.company_name)   # Output: New Corp
Difference: Instance vs Class Variables

Feature	Instance Variable	Class Variable
Defined in	__init__ using self	Class body, outside methods
Scope	Unique to each object	Shared across all objects
Accessed via	self.variable or object.variable	ClassName.variable
Changes affect	Only that specific object	All objects (unless overridden)
5. Encapsulation
Encapsulation is the OOP principle of bundling data and methods that operate on that data within a single unit (class), and restricting direct access to some of the object's components. It protects the internal state of an object from unintended modification.

Encapsulation is achieved in Python using access modifiers (see Section 11) and getter/setter methods.

Example

class BankAccount:
    def __init__(self, balance):
        self.__balance = balance    # private variable

    def get_balance(self):          # getter method
        return self.__balance

    def deposit(self, amount):      # setter-style method
        if amount > 0:
            self.__balance += amount

account = BankAccount(1000)
account.deposit(500)
print(account.get_balance())   # Output: 1500
# print(account.__balance)     # AttributeError — direct access blocked
Advantages of Encapsulation

Advantage	Description
🔒 Data Protection	Prevents unauthorised access to sensitive data
🛡️ Data Integrity	Ensures data is modified only through controlled methods
🧩 Modularity	Internal implementation can change without affecting outside code
🐛 Easier Debugging	Centralised control over data modification
6. Inheritance
Inheritance allows a child class (subclass) to acquire the properties and methods of a parent class (superclass). It promotes code reuse and establishes a natural hierarchy between classes.

Syntax

class ParentClass:
    # parent body

class ChildClass(ParentClass):
    # child body
Example

class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(f"{self.name} makes a sound.")

class Dog(Animal):
    def speak(self):
        print(f"{self.name} says: Woof!")

class Cat(Animal):
    def speak(self):
        print(f"{self.name} says: Meow!")

d = Dog("Bruno")
c = Cat("Whiskers")
d.speak()   # Output: Bruno says: Woof!
c.speak()   # Output: Whiskers says: Meow!
Types of Inheritance

Type	Description	Example
Single	One child inherits from one parent	class B(A)
Multiple	One child inherits from multiple parents	class C(A, B)
Multilevel	Chain of inheritance	class C(B) where class B(A)
Hierarchical	Multiple children inherit from one parent	class B(A), class C(A)
Hybrid	Combination of two or more types	Combination of above
Advantages of Inheritance

♻️ Promotes code reuse — avoid rewriting common logic
🏗️ Establishes clear, logical class hierarchies
🔧 Simplifies maintenance — changes in parent propagate to children
📈 Extensibility — easily extend existing classes with new features
7. Polymorphism
Polymorphism means "many forms." In OOP, it allows the same method name to behave differently depending on the object that calls it. This enables a single interface to represent different underlying data types or classes.

Polymorphism in Python is achieved through method overriding and duck typing.

Example

class Shape:
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

shapes = [Circle(5), Rectangle(4, 6)]

for shape in shapes:
    print(f"Area: {shape.area()}")
# Output:
# Area: 78.5
# Area: 24
Types of Polymorphism

Type	Description
Compile-time (Method Overloading)	Same method name, different parameters — limited native support in Python
Runtime (Method Overriding)	Child class redefines a parent class method
Duck Typing	Python's flexible approach — if it behaves like a duck, it's treated like one
Advantages of Polymorphism

🔄 Increases flexibility and extensibility of code
✂️ Reduces complexity by using a single interface for multiple types
🧩 Enables writing generic, reusable code
8. Abstraction
Abstraction is the OOP principle of hiding complex implementation details and exposing only the essential features of an object. It focuses on what an object does rather than how it does it.

In Python, abstraction is implemented using the abc (Abstract Base Class) module. An abstract class cannot be instantiated directly and must be subclassed with all abstract methods implemented.

Syntax

from abc import ABC, abstractmethod

class AbstractClass(ABC):
    @abstractmethod
    def abstract_method(self):
        pass
Example

from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def start_engine(self):
        pass

class Car(Vehicle):
    def start_engine(self):
        print("Car engine started with a key.")

class Motorcycle(Vehicle):
    def start_engine(self):
        print("Motorcycle engine started with a kick.")

c = Car()
m = Motorcycle()
c.start_engine()   # Output: Car engine started with a key.
m.start_engine()   # Output: Motorcycle engine started with a kick.
# v = Vehicle()    # TypeError — cannot instantiate abstract class
Advantages of Abstraction

Advantage	Description
🎯 Focus on essentials	Hides irrelevant implementation details
🔒 Security	Prevents direct access to internal implementation
🏗️ Enforces structure	Ensures all subclasses implement required methods
🔧 Flexibility	Internal implementation can change without breaking the interface
9. Method Overriding
Method Overriding occurs when a child class provides a new implementation of a method that is already defined in its parent class. The child class method has the same name and parameters as the parent's method, but different behaviour.

Example

class Animal:
    def sound(self):
        print("Some generic animal sound")

class Dog(Animal):
    def sound(self):               # overrides parent method
        print("Dog barks: Woof!")

class Cat(Animal):
    def sound(self):               # overrides parent method
        print("Cat meows: Meow!")

a = Animal()
d = Dog()
c = Cat()

a.sound()   # Output: Some generic animal sound
d.sound()   # Output: Dog barks: Woof!
c.sound()   # Output: Cat meows: Meow!
Key Points

Feature	Detail
Defined in	Child (subclass)
Same name as	Parent method
Parameters	Same as parent method
Effect	Child's version is called, not parent's
Relation to Polymorphism	Core mechanism behind runtime polymorphism
10. super() Function
The super() function is used to call a method from the parent class within a child class. It is most commonly used inside __init__ to initialise the parent class attributes without explicitly naming the parent class.

Syntax

super().method_name(arguments)
Example

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)         # calls Person's __init__
        self.student_id = student_id

    def display(self):
        print(f"Name: {self.name}, Age: {self.age}, ID: {self.student_id}")

s = Student("vimal", 21, "STU001")
s.display()
# Output: Name: vimal, Age: 21, ID: STU001
Advantages of super()

✅ Avoids hardcoding the parent class name
✅ Works correctly with multiple inheritance using Python's MRO (Method Resolution Order)
✅ Promotes cleaner and more maintainable code
✅ Ensures parent class is properly initialised before child adds its own attributes
11. Access Modifiers
Access modifiers define the visibility and accessibility of class attributes and methods. Python uses naming conventions (rather than strict keywords) to implement access control.

Public
Syntax: self.variable
Accessible from anywhere — inside the class, outside the class, and in subclasses.
Default access level in Python.
class Student:
    def __init__(self, name):
        self.name = name    # public variable

s = Student("vimal")
print(s.name)               # Accessible directly — Output: vimal
Protected
Syntax: self._variable (single underscore prefix)
Intended to be accessed only within the class and its subclasses.
Python does not enforce this restriction strictly — it is a convention signalling "internal use."
class Employee:
    def __init__(self, salary):
        self._salary = salary    # protected variable

class Manager(Employee):
    def show_salary(self):
        print(f"Salary: {self._salary}")   # accessible in subclass

m = Manager(75000)
m.show_salary()    # Output: Salary: 75000
Private
Syntax: self.__variable (double underscore prefix)
Accessible only within the class where it is defined.
Python applies name mangling (_ClassName__variable) to enforce restricted access.
class BankAccount:
    def __init__(self, balance):
        self.__balance = balance    # private variable

    def get_balance(self):
        return self.__balance       # accessible via method

account = BankAccount(5000)
print(account.get_balance())    # Output: 5000
# print(account.__balance)      # AttributeError
# print(account._BankAccount__balance)   # Accessible via name mangling (not recommended)
Summary of Access Modifiers

Modifier	Syntax	Accessible From	Convention
Public	self.variable	Anywhere	Default — no restriction
Protected	self._variable	Class + Subclasses	Single underscore — internal use signal
Private	self.__variable	Class only	Double underscore — name mangling applied
💻 Programs Implemented
1. 🎓 Student Management System
Description: A system to manage student records using OOP principles. Demonstrates class creation, constructors, instance variables, and instance methods.

Concepts Used

Concept	Application
Classes & Objects	Student class with multiple objects
Constructors	__init__ to initialise name, roll number, marks
Instance Variables	Each student has unique name, roll, grade
Instance Methods	Methods to display details and calculate grade
2. 🏦 Bank Account System (Encapsulation)
Description: Simulates a bank account with deposit, withdrawal, and balance enquiry features, demonstrating data protection through encapsulation.

Concepts Used

Concept	Application
Encapsulation	Private __balance variable
Access Modifiers	Private attributes with public getter/setter methods
Constructors	Initialises account with holder name and starting balance
Instance Methods	deposit(), withdraw(), get_balance()
3. 👔 Employee Management (Inheritance)
Description: Models an employee hierarchy with a base Employee class and specialised subclasses (Manager, Developer), demonstrating inheritance and method overriding.

Concepts Used

Concept	Application
Inheritance	Manager and Developer inherit from Employee
Method Overriding	Each subclass overrides display_info()
super() Function	Child classes call parent __init__ via super()
Class Variables	Shared company_name across all employees
4. 🚗 Vehicle System (Polymorphism)
Description: Implements a vehicle hierarchy where different vehicle types override a common start_engine() method, demonstrating runtime polymorphism.

Concepts Used

Concept	Application
Polymorphism	Same method name, different behaviour per vehicle type
Method Overriding	Each vehicle class overrides start_engine() and fuel_type()
Inheritance	Car, Bike, Truck inherit from Vehicle
Abstraction	Base Vehicle class defines the interface
5. 📐 Shape Area Calculator (Abstraction)
Description: An abstract Shape class defines a contract for calculating area. Concrete subclasses (Circle, Rectangle, Triangle) implement the abstract method with their own formulas.

Concepts Used

Concept	Application
Abstraction	Abstract Shape class with @abstractmethod area()
Abstract Base Class	Uses Python's abc module
Method Overriding	Each shape implements area() differently
Polymorphism	Shapes processed uniformly through a common interface
6. 📚 Library Management System (Mini Project)
Description: A mini project combining all OOP concepts to simulate a library system. Manages books, members, and borrowing operations.

Concepts Used

Concept	Application
Classes & Objects	Book, Member, Library classes
Encapsulation	Private attributes for book availability and member records
Inheritance	PremiumMember inherits from Member with extended privileges
Polymorphism	borrow_book() behaves differently for regular vs premium members
Access Modifiers	Protected and private attributes used appropriately
Class Variables	Tracks total number of books and members
📁 File Structure
Python-Task-4/
│
├── 📄 student_management.py       # Student Management System
├── 📄 bank_account.py             # Bank Account System (Encapsulation)
├── 📄 employee_management.py      # Employee Management (Inheritance)
├── 📄 vehicle_system.py           # Vehicle System (Polymorphism)
├── 📄 shape_area_calculator.py    # Shape Area Calculator (Abstraction)
├── 📄 library_management.py       # Library Management System (Mini Project)
└── 📄 README.md                   # Project Documentation
🧠 Key Concepts Covered
#	Concept	Description
1	Classes	Blueprint for creating objects with shared structure and behaviour
2	Objects	Instances of a class with their own unique state
3	Constructors (__init__)	Special method to initialise object attributes at creation
4	Instance Variables	Data attributes unique to each individual object
5	Instance Methods	Functions that operate on instance-specific data via self
6	Class Variables	Shared attributes common to all instances of a class
7	Encapsulation	Bundling data and methods; restricting direct access to internal state
8	Inheritance	Child class acquiring properties and methods from a parent class
9	Polymorphism	Same method name exhibiting different behaviour across classes
10	Abstraction	Hiding implementation details; exposing only essential interfaces
11	Method Overriding	Child class redefining a parent class method with new behaviour
12	super() Function	Calling a parent class method from within a child class
13	Public Access	Attributes accessible from anywhere
14	Protected Access	Attributes intended for class and subclass use (_variable)
15	Private Access	Attributes restricted to the defining class only (__variable)
✅ Conclusion
This task provided a thorough and practical understanding of Object-Oriented Programming (OOP) in Python — one of the most essential paradigms in modern software engineering. Through a series of progressively complex programs, all four core pillars of OOP were explored and applied:

🔒 Encapsulation — through the Bank Account System, demonstrating how to protect sensitive data using private attributes and controlled getter/setter methods.
🧬 Inheritance — through the Employee Management System, demonstrating how code is shared and extended across a class hierarchy without duplication.
🔄 Polymorphism — through the Vehicle System, demonstrating how a common interface can produce varied behaviour depending on the object type.
🎭 Abstraction — through the Shape Area Calculator, demonstrating how abstract classes enforce a contract while hiding complexity from the user.
The Library Management System served as a comprehensive mini-project, bringing all concepts together into a cohesive, real-world application.

Writing programs with OOP principles makes code more modular, scalable, and maintainable. These skills form a critical foundation for advanced topics like design patterns, frameworks, and enterprise-level software development.

💡 Object-Oriented Programming is not just a coding style — it is a way of thinking that mirrors how the real world is structured. Mastering OOP is mastering the foundation of professional software engineering.

👨‍💻 Author
vimal kumar

Python Internship Program — Task 4

Made with Python OOP Internship
