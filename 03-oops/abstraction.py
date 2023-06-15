from abc import ABC, abstractclassmethod

class Car(ABC):
    @abstractclassmethod
    def mileage(self): #different implementation in class and sub classes--> abstract method
        pass
    def color(self): # same implementation in all sub classes-->concreate method
        print("while")
    
class Maruti_Suzuki(Car): # if we can't define abstract method then it will through an error
    def mileage(self):    # so if we don't define abstract method in child class, so child class will become abstract Class
        print("Mileage is 30 kmph")
    
class TATA(Car):
    def mileage(self):
        print("Mileage is 35 kmph")

class Duster(Car):
    def mileage(self):
        print("Mileage 40 kmph")

#we can't create Object for abstract class
# c1 = Car() --> !!ERROR- can't create instantiate abstract class Car  


m1= Maruti_Suzuki()
t1= TATA()
d1=Duster()

t1.mileage()
t1.color()


print("**ABSTRACT**")
from abc import ABC, abstractmethod
class BankApp(ABC):
    def database(self):
        print("connected to abstract")

    @abstractmethod
    def security(self):
        pass
    @abstractmethod
    def display(self):
        pass

class MobileApp(BankApp):
    
    def mobile_login(self):
        print("login into mobile")

    def security(self):
        print("Mobile security")

    def display(self):
        print("Mobile disply")

mob = MobileApp()
mob.security()


