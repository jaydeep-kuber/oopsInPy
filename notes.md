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
> class Car:
>    def carPrice(self):
>     # logic
> BMW = Car()
> BMW.carPrice()  <- here in secret hidden python pass `Car` obj in `self` arg that's why it is fixed at 1st position.  