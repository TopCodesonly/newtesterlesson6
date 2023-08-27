# We can open, close, read, write or  preform any other kind of work with file using python.
#There are several modes from which we can open a file


# r >> read file
# w >> write in the file
# a >> append mode
# r+ >> read and write mode
# w+ write and read mode
# x >> exclusive write mode
# a+ append and read


filename="message.txt"
fp=open(filename,"w")
fp.write("Maulik is awesome")
fp.close()


fp=open(filename,"r")
read=fp.read()
print(read)
print(type(read))
fp.close()
# # closing the file is important as it protects the system from memory leekagage.
# #but sometimes we may forget to cllock the file
# #So, it is better to open a file with context manger

with open(filename,"a") as fp:
    fp.write("\nI am great")

with open(filename, 'r+') as fp:
    data=fp.read()
    fp.seek(0) # it puts the file pointer to the top of the file
    fp.write("hi")


with open(filename,"w+") as fp:
    fp.write("I am a amzing coder/gunius")
    fp.seek(0)
    data=fp.read()
    print(data)

with open(filename,"x") as fp:
    fp.write("hello")
