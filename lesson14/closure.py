#closure is the concept in python which fulfils the following:
#1. there sould be nesed function(a function in a another function)
#2. An inner function my reference the argument from outher function
#3.other function should return the inner function

def closure_fxn(meeg):
    def inner_fxn():
        print(meeg)
    return inner_fxn


result=closure_fxn("hello_world")
print(result)

# the abouve function is the simplest closure that can be made in python. closures are basis of decoratores in python
