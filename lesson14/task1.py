#Creating a function that takes message and simply return the text message
# create a decorater which changes text message into upper case text
def upper(func):
    def inner(*args,**kwargs):
        return func(*args,**kwargs).upper()
    return inner
@upper
def message(txt):
    return txt

print(message)