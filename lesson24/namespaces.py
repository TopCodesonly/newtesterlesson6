# #Namespaces determine the scope of the varibles and objects in python
#Namespaces is explate d by LEGB rule (Local, Enclosed, gobal ,builtin)
# #There are 4 types of namespaces
#     #1.Local Scope
#     #2. Enclosed Scope
#     #3.Gobal Scope
#     #4. Built-in Scope

# #Bulit--n scope 
# # If the scope of pakage or object is all over the project then is is an object of built-n scope
# # Example: Python built-in libraries like math, os,json etc.
# # import math  #Built-in Scope




# #Gobal Scope
# #If the scope of the variable or obeject is limited to one python module then it has a global scope to that module

# b=11# This variable 'b' is limited to this python file only 
# print(b)




# #Local Scope
# # If the variable scope is limited  to a function then it has local scope 

# a=12
# def test_func():
#     a=20
#     print(a)#Local scope
# print(a)#12

# test_func()#20
# print(a)#12




#Enclosed Scope
#If the scope of the variable or object is limited to a nested function the it has an enclosed scope

# a=12 #Gobal scope
# def outer_fux():
#     a=20#Local scope
#     def inner_inn():
#         a=30# Enclosed Scope
#         print(a)#30
#     inner_inn()
#     print(a)#20

# print(a)#12
# outer_fux()
# print(a)#12
        
# #12,30,20,12


#But, We have a "gobal" keyword which can define even a local varibable as a global

a=11
def outer_func():
    global a
    a=40
    def inner_func():
        a=30
        print(a)#30
    inner_func()
    print(a)#40
print(a)#20
outer_func()
print(a)#40

#11 30 40 40

#Non-local keyword