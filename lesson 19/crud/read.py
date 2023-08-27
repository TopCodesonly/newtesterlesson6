import json

filename="students.json"


def read_student(student_id):
    with open(filename,"r") as fp:
        students=json.loads(fp.read())
    students=list(filter(lambda x: x['id'] == student_id, students))
    if students:
        student=students[0]
        print(student)
    else:
        print("No student")
    repeat=input("do you want to cointinue (y/n)")
    return True if repeat.lower() == 'y' else False
        
        