import json
import os
filename = "students.json"


def create_student():
    id = input("Enter student id ")
    name = input("Enter student name ")
    age = input("Enter student age")

    student = dict(id=id, name=name, age=age)
    if not os.path.exists(filename):
        with open(filename, "w") as fp:
            data = json.dumps([student],indent=2)
            fp.write(data)
    else:
        with open(filename,"r+") as fp:
            students=json.loads(fp.read())
            students.append(student)
            fp.seek(0)
            fp.write(json.dumps(students,indent=2))
    print("Student Added Successfully !!")
    repeat=input("Do you want to continue (y/n)")
    return True if repeat.lower() == 'y' else False