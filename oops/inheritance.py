class Employee:
    bonus = 2000
    def display(self):
        print("This is employee class method")


class Manager(Employee):  # child class, it can access parent class and child class object
    bonus1= 5000
    def show(self):
        print("This is a manager class method")


e1 = Employee()
m1 = Manager()

e1.display()
m1.show()
print(m1.bonus)
print(e1.bonus1)