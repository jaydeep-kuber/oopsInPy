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