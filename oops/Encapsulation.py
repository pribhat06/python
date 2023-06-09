class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def display(self):
        print(f"name is :{self.name} and salary is : {self.salary}")


obj = Employee("Pri", 90000)
obj.display()

print("****************")


class Finance:
    def __init__(self):
        self.revenue = 100000
        self.number_of_sales = 114

f1 = Finance()
print(f1.__dict__)
class HR:
    def __init__ (self):
        self.number_of_emp = 32
        f1.revenue = 1


h1 = HR()
print(f1.__dict__)