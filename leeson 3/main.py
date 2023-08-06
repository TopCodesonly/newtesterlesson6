# #append()

# # ECTEND()


# a=[1,2,3] 
# b=[4,5,6]

# result=a.extend(b)


# #insert(index,value)

# vowels=['a','e','i']
# vowels.insert(1,'t')
# print(vowels)


# # pop takes index a parameter 
# vowels=['a','e',]
# result=vowels.pop(1)
# #by dealtft takes last 



# # clear clear the list  

# #index(value start end)

# vowels=['a','e','i']

# res=vowels.index("i")
# print(res)

# # count count the number of element how many times the value 2 is in the list 



# #sort(trver=)

# a=[1,5,6,7,5,6,65]
# a.sort
# a.sort(reverse=True)

# print(a)
# #

# a=[(5,4),(3,2),(432,4645),(45,12)]
# #output >> 


# def secnum(data):
#     return data[1]

# a.sort(key=secnum)


a=[(4,12,5),(6,1),(11,12),(6,7,8)]
def to(data):
    return data[-1]
a.sort(key=to)

print(a)