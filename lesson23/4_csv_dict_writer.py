import csv

students=[{'id': '1', 'name': 'Jon', 'age': '30', 'address': 'ktm'},
           {'id': '2', 'name': 'Mateo', 'age': '13', 'address': 'NY'}, 
           {'id': '3', 'name': 'jack', 'age': '99', 'address': 'AS'},
           {'id': '5', 'name': 'Mat', 'age': '14', 'address': 'FR'},
           {'id': '6', 'name': 'teo', 'age': '15', 'address': 'AG'}]

filename='write_student.csv'

with open(filename,"w") as cw:
    field_names = students[0].keys()
    csv_writer=csv.DictWriter(cw,fieldnames=field_names)
    csv_writer.writeheader()
    for student in students:
        if student["age"] < "25":
            csv_writer.writerow(student)
