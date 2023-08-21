#Opp is an apporact of programming in which programs are medeled in the real world problem
# OOP stands for object-oriented programming 
# it has two major aspects; class and objects
# class is the blueprint of an object. It has its own attributes known as properties and metholds
#Objects are the instance of a class

# there are four major pillars of OOP:
    #1.Inheritace
    #2.Encapsulation
    #3.Polymorphism
    #4.Abstaction

class motors:
    engin_type = "Hybird"
    speed="190km/h"
    def __init__(self,nod,colors,num_of_models):
        self.nod=nod# intace attribute
        self.colors=colors#instance attribute
        self.num_of_models=num_of_models
    def descirption(self):
        return f"THe engin type is {self.engin_type}, there are {self.nod} door the color is {self.colors} there are {self.num_of_models} number of models of this veacails the max speed is {self.speed}"

Motors1=motors(4,"red",9)
print(Motors1.engin_type)
print(Motors1.speed)
print(Motors1.nod)
print(Motors1.colors)
print(Motors1.num_of_models)

print(Motors1.descirption())


#In this vehicle class "engine_type" is a class attribute, color and number of doors etc


# In this vehicle class "engin_type" is a class attribute color and  numbers  of doors are instace 
# attributes ...

#let set attributes in the objects
Motors1=motors(4,"black",4)
print(Motors1.colors)# black getting value from the object
Motors1.colors="green"
print(Motors1.colors)# green setting value in the object