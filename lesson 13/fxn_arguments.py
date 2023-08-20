#Order of the functions arguments is improtant to note
# arguments are the values passed during funchtion call and parameters are the
#values taken in function definition

#order of the arguments
#1. Positional/ Compulsory Arguments
#2. Deafault Arguments
#3.Arbitary Arugments

def add(a,b,c=10): # here 'a' and 'b' are the  positional arguments
    return a+b+c
print(add(5,5,c=5)) # here c is a new keyyword argument

# if we send value in the function call then the default value always get override
#here c=5 overrrides 10

# arbitary arguments can take random number of elements in the function call. they are like an expandable bucket 


def add(*args):
    print(args)
    return sum(args)

print(add(1,2,3))
print(add(1,2,3,4,5))
print(add(1,2,3,4,5,6,7))


def add(**kwargs):
    print(kwargs)
    print(type(kwargs))
    return sum(kwargs.values())

print(add(a=1,b=2,c=3))
print(add(a=4,b=5,c=6))


# arbitrary arguments also have their own order. *args sould always come before than **kwargs

def add(a,b,c,d=1,e=2,f=3,*args,**kwargs):
    print(a)
    print(b)
    print(c)
    print(d)
    print(e)
    print(f)
    print(args)
    print(kwargs)
print(add(4,5,6,7,8,9,10))