# Take two numbers as input and add those numbers. Handle the possible exceptions.

# try:
#     num1=int(input("enter a number"))
#     num2=int(input("enter a number"))
#     ans=num1+num2
#     print(ans)
# except Exception as m:
#     print(m)
#     print("An error has been raised try entering a interger;")

# else:
#     print(ans)
# finally:
#     print("this is your answer")
    


#Take two numbers input and divide a number by another number. Handle the possible exceptions.

# try:
#     num1=int(input("enter a number"))
#     num2=int(input("enter a number"))
#     ans=num1/num2
#     print(ans)
# except Exception as m:
#     print(m)
#     print("An error has been raised try entering a interger;")

# else:
#     print(ans)
# finally:
#     print("this is your answer")


#Create a dictionary student with keys id, name, age, department. Take a input from the user, 
#which info (id, name, age or department) he wants to access and print the result. Handle the possible exceptions.


# dict1={'id':"1234434",'name':"Max","age":"13","department":"Art"}
# print(dict1.values())
# print(dict1.keys())
# try:
#     finder=input("enter the key you are looking for")
#     data = dict1[finder]
    
# except:
#    print("make sure you are writing the correct key")
# else:

#     print('the',finder,"of the student is",data)

#Create a function to check whether a input character is vowel or not. Handle the possible exceptions.
letter=input("enter the letter")


def is_vowel(letter):
    if any([letter.isnumeric(),len(letter)>1, type(letter) != str]):
        return letter.lower() in ['a','e','i','o','u']
    return True
        

result= is_vowel(letter)

print(result)