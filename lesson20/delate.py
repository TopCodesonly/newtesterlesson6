from estd_connection import estd_connection

cursor=estd_connection()



id=input("enter student id")



sql= f""" DELETE FROM STUDENT WHERE ID= '{id}'"""

cursor.execute(sql)
print("SUCCESFULLY DELATED")