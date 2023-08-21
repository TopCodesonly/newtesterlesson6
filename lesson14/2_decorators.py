def decorate_me(func):
    def inner_fnx(*args,**kwargs):
        print("extra")
        return func(*args,**kwargs)
    return inner_fnx
@decorate_me
def message(txt):
    return txt

#result=decorate_me(message)
print(message("hello world"))

@decorate_me
def message2(txt,txt2,txt3="deafult"):
    return txt,txt2,txt3

print(message2("hello","world",txt3=",Maulik here"))