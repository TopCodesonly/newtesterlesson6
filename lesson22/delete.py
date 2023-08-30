from estd_connection import estd_connection

cursor=estd_connection()

def delete_student(student_id):
    
    sql= f""" DELETE FROM STUDENT WHERE ID= '{id}'"""

    cursor.execute(sql)
    print("SUCCESFULLY DELATED")
    repeat=input("Do you want to continue (y/n)")
    return True if repeat.lower() == 'y' else False