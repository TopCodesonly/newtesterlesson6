vowels=["a","e","i","o","u"]
for each in vowels:
    print(each)

# looping in similar to



student={"name":"john", "age":23,"address":"ktm"}
print(student.keys())
print(student.values())
for value in student.values():
    print(value)

# looping through both dictinary key and value
print(student.items()) 


spquared_dict={k: k**2 for k in range(1,6)}
# diccompresence


student_list=[("name","john") ("age","25") ("address","ktm")]
print(student_list.keys())