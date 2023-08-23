#classmethods are the methods which takes class as the first parameter rather than self
#classmethold is created @classmethod decorator
#Static methods are the metholds which neither takes class nor self as a parameter. they are like 
# a normal function which doesn't change the state of the class
# Static method is created using @static method decorator

class student():
    def __init__(self,age): 
        self.age=age
    @classmethod
    def from_birth_year(cls,year):
        age=2023-year
        return cls(age)
    @staticmethod
    def alices():
        return "human"
        

s1=student(25)  
print(s1.age)
s2=student.from_birth_year(2010)
print(s2.age)
print(s2.alices())
#Here "from_birth_year method is a class method. and it is also sometimes termed as a factory method"
