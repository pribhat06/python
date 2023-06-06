from abc import ABC, abstractclassmethod

class Car(ABC):
    @abstractclassmethod
    def mileage(self):
        pass
    def color(self):
        print("while")
    
class Maruti_Suzuki(Car):
    def mileage(self):
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