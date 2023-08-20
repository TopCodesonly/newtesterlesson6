# A funchtion that takes another function as an argument is called higher order function
# sorted(), map(),fliter(), ruduce(), decorators etc. are the gifher order function in python

# map(function,iterable)
# map takes function as first parameter and iterable as a second parameter
# it maps every elements of the iterable to some other form
# the lenght of interial interable and final result is same in map

data=[15,2,3,4]
def cubed(elem):
    return elem **3

res=map(cubed,data)# <map_object which is an iterator and can be looped. but to see its element we need to covert it to some other datatype
print(list(res))

x=lambda cubed: map(cubed,data)
print(x)
# fliter()
#it also takes function and iterable as arguments
# it picks certain elements from the initals iterable
#but the size of inital iterable and fubal result may not be same in case of filter

data=[1,2,3,4,5,6,7,8,9,10]
def get_even(x):
   return x % 2==0
    
res=filter(get_even,data)
print(res)
print(list(res))


# ruduce()
#it also takes function and iterable as arguments
# it does operation based on the function and return a single value
from functools import reduce
data=[1,2,3,4,5,6]
def add(x,y):
    return x+y

res=reduce(add,data)
print(res)#21

# the job ruduce is to give single result ...