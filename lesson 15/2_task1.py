class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def get_details(self):
        return f"my name is {self.name}, I am {self.age} years old."
p1=Person("red",9)
print(p1.get_details())

print(E.mro())