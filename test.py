class Person:
    "A very simple class"
    def __init__(self,name, yy):
        self.name = name
        self.age = yy




a_person =Person("HAUWA'U ",48)
print(a_person.name)
print(a_person.age)


# class attribute
print(Person.__name__)
print(Person.__doc__)
print(Person.__bases__)
print(Person.__module__)
print(Person.__dict__)


# instances attribute
print(a_person.__class__)
print(a_person.__doc__)