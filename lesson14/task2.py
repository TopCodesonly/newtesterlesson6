# create a decortor "login"

def login(func):
    def inner(*args,**kwargs):
        password=input("enter your password")
        if password == '1234':
            return func(*args,**kwargs)
        else:
            print("your password is invalid")
    return inner

@login
def addtion(a,b):
    return a+b

print(addtion(10,1))