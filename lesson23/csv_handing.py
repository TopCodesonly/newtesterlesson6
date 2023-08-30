#CSV stands for comma sparated values

# CSV files have extension .csv
import csv
filename="lesson23/students.csv"

with open(filename,"r") as cr:
    csv_reader=csv.reader(cr)
    # for each_line in csv_reader:
    #     print(each_line)

    result=[]
    for count,each_line in enumerate(csv.reader(cr)):
        if count == 0:
            continue
        data=dict(id=each_line[0],name=each_line[1],age=each_line[2], address=each_line[3])
        result.append(data)
print(result)





