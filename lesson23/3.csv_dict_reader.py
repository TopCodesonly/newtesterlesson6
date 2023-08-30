
import csv

filename="lesson23/students.csv"
result=[]

with open(filename,"r") as cr:
    for each in csv.DictReader(cr):
        result.append(each)

print(result)