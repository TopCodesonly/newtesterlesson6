#Encapsulation is the process of data huding in OOP approoach of programming

#We can make the attributes private,pubic,or protected.

#In python, protect members can be created using a single underscore (_) 
#and private member can be created using double underscore(__)'

class Vehicle:
    _color="blue"

    def __init__(self,doors,engin):
        self._doors=doors
        self._engin=engin

    def description(self):
        return f"the color of the vehicle is {self._color}. There are {self._doors} number of doors and the maxspeed is {self._engin} "

    def set_color(self,color):
        self._color=color
    
    def get_color(self):
        return self._color

m1=Vehicle(4,"Hybrid")
print(m1.description())
print(m1._color)
m1.set_color("green")
print(m1.get_color())

# Protected members of a clas are meant to be used within a class or in their children class only
# they are non member 




#Private property is not accesoble outside the or in children classes
#print(v1._mileage)# it raises  attribute error mileage is a private property

print(m1._engin)