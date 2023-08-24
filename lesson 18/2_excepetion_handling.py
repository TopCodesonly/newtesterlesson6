#try and except

# try:
#     num = int(input("enter a number"))
# except:
#     print("An error has been raised try entering a interger;")

# # #We can specicy the error type in the except statement to chech the specific type of error
# try:
#     num = int(input("enter a number"))
# except ValueError:
#     print("An error has been raised try entering a interger;")

# #We can catch mulitiple exception using the same except block

#     num = int(input("enter a number"))
# except (ValueError,KeyError,TypeError):
#     print("An error has been raised try entering a interger;")



#try ... except... else... finally block

#Else block is executed when no error occurs in the try block
#Finally block is always executed no matter there is an error or not 

try:
    num = int(input("enter a number"))
    num2 = int(input("enter a number"))
except Exception as f:
    print(f)
    print("An error has been raised try entering a interger;")
else:
    add=num+num2
    print("the sum is",add)
finally:
    print("this block is always excuted ")