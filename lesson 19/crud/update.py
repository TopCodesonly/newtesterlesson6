import json

filename='students.json'

def update_student(student_id):
    with open(filename,"r+") as fp:
        students=json.loads(fp.read())
        student=list(filter(lambda x: x['id'] == student_id,students))
        if student:
            student=student[0]   #
            index=students.index(student)
            key=input("Enter the infomation you want to update")
            new_val=input("enter the new value")
            
            student[key]=new_val
            students[index]=student
            fp.seek(0)
            fp.write(json.dumps(students,indent=2))
            print("student updated succesfully")
        else:
            print("enter a valid student id")
    repeat=input("do you want to cointinue (y/n)")
    return True if repeat.lower() == 'y' else False


            
