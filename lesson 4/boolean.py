# # mebership operation

# print("a" in ["a","e","i"])
# print("a" not in ["a","e","i"])

# #indentiy operation 


# a=1
# b=1
# print(a  is b) # true 
# print(a  is not b) #false






# print(a is not b)
# print(id(a) != id(b))






# ######## Concept of truly and falsey #=:

# a=5
# print(not a)


# # any non-zero or non-empty including True inself is turthy data type 
# # 5,1,0,-2 [1,2] (3,4) {5,6,'g'} {'a;:1} True alse thse data truthy data types


# # in contrst all empty data types zero and none including false are falsey datatypes
# # 0,[].(),{},set(),"",None,False; all thse are falsy data types

# # to verify if it is turty or falsy 

a=4
b=-3
c=[1,2,3]
d=(1,2)
e={1,2}
f={"a":1}
g="hello"
h=True

print(bool(a))
print(bool(b))
print(bool(c))
print(bool(d))
print(bool(e))
print(bool(f))
print(bool(g))
print(bool(h))
print(bool(True))

#ans True
"""True
True
True
True
True
True
True
True"""


# applying not operation to any truthy value results in false

print(not a)#false



#check for falsy
#same but empty
# it will be all false

# applying not operation to any falsy value results in True

print(not a) #True

print(not None) # False

############### python boolean is a sub-class of interger

# True is integer 1 and false is interger 0

