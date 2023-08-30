from estd_connection import estd_connection

cursor=estd_connection()
def create_student():
    id=input("enter student id")
    name=input("enter student name")
    age=input("enter student age")
    sql= f""" INSERT INTO STUDENT(ID,NAME,AGE) VALUES ('{id}','{name}', {age})"""
    


    cursor.execute(sql)
    print("tble has been made")
    repeat=input("Do you want to continue (y/n)")
    return True if repeat.lower() == 'y' else False