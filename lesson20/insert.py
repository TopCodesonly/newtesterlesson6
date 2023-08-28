from estd_connection import estd_connection

cursor=estd_connection()


sql="""
CREATE TABLE STUDENT(
    ID CHAR(20),
    NAME CHAR(20),
    AGE INT
)"""

id=input("enter student id")
name=input("Student name")
age = int(input("enter student age"))


sql= f""" INSERT INTO STUDENT(ID,NAME,AGE) VALUES ('{id}','{name}', {age})"""

cursor.execute(sql)
print("table has been made")