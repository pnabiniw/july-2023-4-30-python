import json
filename = "students.json"


def create_student():
    id = input("Enter student id ")
    name = input("Enter student name ")
    age = input("Enter student age")

    student = dict(id=id, name=name, age=age)
    with open(filename, "w") as fp:
        data = json.dumps(student)
        fp.write(data)
    print("Student Added Successfully !!")
