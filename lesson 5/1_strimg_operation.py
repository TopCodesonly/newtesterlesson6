#Concatenation Concat
#+


#Repetitions/ Broadcast operations >>> Broadcast is

message="hi"
print(message*5)#hi hi hi hi hi hi 

print("h" in message)#True
print("h" not in message)#false


# BUILT IN FUNCTION

#use of len




# use of slice >>> This function simmlar string and list slicling
# message="hi"
# sliced_data=slice[2:7]
# print(message[sliced_data])



# split()

# message="Hello coders I am awesome!!"
# result=message.split() # without parmameter
# print(result)#['Hello', 'coders'] ['Hello', 'coders', 'I', 'am', 'awesome!!']
# result=message.split("o")
# print(result)#['Hell', ' c', 'ders I am awes', 'me!!']
message="hello,all,I,am,learning,python"
rusult=message.split(",")
print(rusult)#['hello', 'all', 'I', 'am', 'learning', 'python']


#Join

info=['hello', 'all', 'I', 'am', 'learning', 'python']
result="+".join(info)
print(result)#hello+all+I+am+learning+python
info=['hello', 'all', 'I', 'am', 'learning', 'python']
result=", ".join(info)
print(result)#hello,all,I,am,learning,python

#find()
message="Bonjour Mon Ami"
result=message.find("m")
print(result)#13 only fisrt index
message="Bonjour Mon Ami"
result=message.find("ami")
print(result)
#-1 if minus one not found error <<< meaning

sec="ami"

result=message.lower().find(sec.lower())
print(result)#12

#replace()

message="hello world"
result=message.replace("hello","hola") #>> in the parameter enter the the old value first then the the new value
print(result)#hola world


