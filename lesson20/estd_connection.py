#If we want to connect database from a program (python,javascript) then we need a database connector
#we need a database 


import psycopg2
def estd_connection():
    
    conn=psycopg2.connect(
        database="studentdb",
        user="postgres",
        password="maulik",
        host="127.0.0.1",
        port=5432
    )


    conn.autocommit= True
    print("Connect established I am working")
    cursor=conn.cursor()
    return cursor

if __name__ == "__main__":
    estd_connection()