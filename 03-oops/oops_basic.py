# A Class is like an object constructor, or a "blueprint" for creating objects.
class Person:
    # The __init__() function is called automatically every time the class is being used to create a new object.
    # class constructor
    # The self parameter is a reference to the current instance of the class, and is used to access variables that belong to the class.
    def __init__(self, num) -> None:
        # class variable, accessible using self
        self.n = num
        print(f"Class object created : {self.n}")
        self.print_var()

    def print_var(self) -> None:
        # normal variables not accessible from other class methods
        # only class variables can be accessed using self parameter
        # print(f"not a class variable : {num}")
        print(f"class variable (self.n) : {self.n}")


# class object : instance of the class
print("\n** creating class object 1")
obj1 = Person(1)
print("\n**creating class object 2")
obj2 = Person(2)

print("\n** modifying class object 1")
obj1.n = 30
obj1.print_var()


#all the methods are instance
#we can access class variable using Class.variable or self.variable

#show all the valiables inside the Class
print(obj1.__dict__)


