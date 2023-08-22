# inheritacnce is the process of accesing the attributes in a parejtnclass by children clases
#Types of inhertance 







#Single inheritance
class A:
    a=11
class B:
    a=26

obj=B()
print(obj.a)#26

class C(A,B):
    pass
obj=C()
print(obj.a)#11

#Mulitilevel inheritance

class A:
    a=10
class B(A):
    a=10
class C(B):
    pass


# Hierarchical Inheritance
class A:
    a=5
class B(A):
    pass
class C(A):
    pass

#Hybrid Inheritance
#it is the combination 


class A:
    a=10
class B(A):
    pass
class C(A):
    pass
class D(B,C):
    a=5
class E(D):
    pass

obj=E()
print(obj.a)#6

print(E.mro())
#  MRO = MRO stands for Methold Resolution Order. It is the order in which attributes in an inherutance
# is accessed rrom the child class