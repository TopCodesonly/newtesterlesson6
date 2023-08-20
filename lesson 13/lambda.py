# lambda are elegant way of creating one-liner function
# lambda function do not have name. So they are also called anonymous function 


def squared(num):
    return num**2
print(squared(2))

squared=lambda num: num**2
print(squared(4))#16


#map()

data=[1,2,3,4,5,6,7,8,9,10]
res=map(lambda elem: elem **3,data)

print(res)
print(list(res))

# filter()
data=[1,2,3,4,5,6,7,8,9,10]
res=filter(lambda x:x% 2==0,data)
print(list(res))


#reduce()
from functools import reduce
data=[1,2,3,4,5,6,7,8,9,10]

res=reduce(lambda x,y:x+y,data)
print(res)#55