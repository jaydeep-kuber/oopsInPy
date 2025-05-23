# Notes 
#### Py OOP Concepts:
    - Atributes & Objs
    - Method Kinds
    - Encaptulation
    - Inheritance
    - Polymorphism
    - Abstraction

- By Default, pyhon sends an object to class methods, that's why we are writing self as the first parameter in methods.

> **what i mean by above sentese ?**
```py 
    class Car:
        def carPrice(self):
        # logic
    BMW = Car()
    BMW.carPrice() #<- here in secret/hidden python pass `BMW` obj in `self` arg that's why it is fixed at 1st position. It was  ok if you call iy by other names but python will always pass the obj of class in 1st position. and it is suggested to not mess with conventions 

```
- ** accessig an attribute of an object**
- So while we are accessing an attribute of object program will first try to get it intance level if attribute wont found at this level then it goes to class level and at the end it is an error.

> Magic attribute getter: `__dict__`
- this is a built-in attribute of an object that holds all the attributes of an object. **what do i mean by this ?** so basically you can get all attrbutes of a class / instanse by using this magic method. 
- **How?**
```py
# ref above car class,
BMW = Car()
print(BMW.__dict__) # this gives instase level attributes
print(Car.__dict__) # this gives class level attributes
```

- to store all instanse in a list we need `all= []` var and in `__init__` method use `Car.all.append(self)` method to add each instanse in list.

```py
class Car:
    all = []
    def __init__(self):
        # logic
        Car.all.append(self)
BMW = Car()
print(Car.all)
```

- **Decorator** : decorator is an annotation on a function that can be used to extend the behavior of the function without permanently modifying it.

> `@classmetod` : this decorator use to make any instance method as class method. so that it can be called without creating an instance of class. and it will be called on class level. here `self` is replaced by `cls` in class method. in backgroud `cls` will passed.
```py
# something like 
class Car:
    @classmethod
    def ClassFunction(cls):
        # logic
        
Car.ClassFunction()
```

- static methods, they are like same a class methods but in background it won't pass class object so we can access this method like a regular method. 
```py
class Car:
    @staticmethod
    def StaticFunction(arg1,arg2,...): # <-- note here we do not need to add `self` or `cls` here.
        # logic
```

#### Inheritance
- **Inheritance** : Inheritance is a mechanism in which one class can inherit the properties of another class. The class that is being inherited is called the parent class or the superclass, and class that is doing the inheriting is called the child class or the subclass.

```py
class Parent:
    def __init__(self):
        self.parent_attr = "Parent"
        # logic
class Child(Parent): # <- this is how we inherit parent class
        def __init__(self):
        super().__init__()
        self.child_attr = "Child"
        # logic
```

> to access the class name from instance we use `__class__.__name__`
> to make read only attribute we use `@property` decorator basiaclly it works as **getter method**.
> to make a variable semi private e.i. you can not change value but can access over instence we use `_` prefix.
> to make a variable full private e.i. you can not change value and can not access over instance we use `__` prefix. 

```py
class Car:
  def __init__(self): 
    # logic  
 @property
    def name(self):
        return self.__name
```

- **For settre method** we use `@name.setter` (refer above given example for `@name`) here `.setter` is important