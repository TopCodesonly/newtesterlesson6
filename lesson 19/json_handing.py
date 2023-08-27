#JSON stadns for javascript object notation
#JSON is a file format with .json extension which is used to share the data 
#and information over the internet
#python has a built-in module for json handing
#JSON is similar to python dictionary as it is also written in key value format
#but, keys and values in JSON data must be enclosed in double-quotes
#Single quotes are not allowed 
#This dose not apply for interger and numbers

#Some examples of JSON data

{"Name":"Maulik","age":13,"address":"KTM"}#valid json
{'Name':'Maulik','age':13,'address':'KTM'}#Invalid JSON because of single quotes


[

    {"Name":"Maulik","age":13,"address":"KTM"},
    {"Name":"Yanvi","age":7,"address":"FRC"}
]


import json
filename="student.json"
student= {"Name":"Maulik","age":13,"address":"KTM"}
students=[

    {"Name":"Maulik","age":13,"address":"KTM"},
    {"Name":"Yanvi","age":7,"address":"FRC"}
]


with open(filename,"w+") as fp:
    data=json.dumps(students,indent=2)
    fp.write(data)
    fp.seek(0)
    data=json.loads(fp.read())
    print(data)
