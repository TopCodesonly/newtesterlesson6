#Polymorphism in Python refers to many forms of the same function or orjects.
#sum(), len(), max() and min() etc. there are some of the examples  which follows polymorphism.
#These built-in function can take different datatypes and performs repective tasks.


# There are two important aspects of Polymorphism.
#1. Function/Methold Overloading
#2. 


#In the Langauge of python, you can do overloading it only takes the latest conmmand

#Although we can give deafault arguments so that we can pass both two and three arguments in the function call


class employment:
    salary=1200
    def description(self):
        return self.salary
    def description(self):
        return f"Salary is {self.salary}"

e=employment()
print(e.description())