def decorate_me(func):
    def inner_fnx(txt):
        print("extra")
        return func(txt)
    return inner_fnx
@decorate_me
def message(txt):
    return txt

#result=decorate_me(message)
print(message("hello world"))