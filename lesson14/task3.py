import time

print(time.time)
start=time.time()
def ex(func):
    def inner(*args,**kwargs):
        
        return func(*args,**kwargs)
    end=time.time()
    print(end-start)
    return inner


@ex
def text(txt):
    x=time.time
    for i in range(10000):
        continue
    return txt

print(text("hi"))
