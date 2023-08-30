filename = "message.txt"

# with open(filename, "w") as fp:
#     fp.write("Hello World\nI'm Learning Python")


# read()
# seek()
# readline()
# readlines()
# tell()
# writelines()
with open(filename, "r") as fp:
    data = fp.read()
    print(data)   #Hello \nI am awesome

    fp.seek(0)#Seek() method changes the cursor of the file
    data = fp.read(12)# Hello w
    print(data)#Hello I am
    
    fp.seek(0)
    data=fp.readline()
    print(data)#I Hello 
 
    fp.seek(0)
    data=fp.readlines()
    print(data)#['Hello \n', 'I am awesome']


data=["Hello Humans\n", "I am awesome\n", "I Know I am great"]

with open(filename,'w') as fp:
    fp.writelines(data)

data=["\n\nHello Humans\n", "\nI am awesome\n", "\nI Know I am great"]

with open(filename,'a') as fp:
    fp.writelines(data)