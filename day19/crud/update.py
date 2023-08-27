import json
filename = 'students.json'


def update_student(student_id):
    with open(filename, "r+") as fp:
        students = json.loads(fp.read())
        student = list(filter(lambda x: x['id'] == student_id, students))
        if student:
            student = student[0]   # {"id": 1, "name": "Jon"}
            index = students.index(student)  # 0

            key = input("Enter info you want to update ")
            new_val = input("Enter the new value ")
            student[key] = new_val  # {"id": 1, "name": "Jane"}
            students[index] = student  # students[0] = {"id": 1, "name": "Jane"}
            fp.seek(0)
            fp.write(json.dumps(students, indent=2))
            print("Student Updated Successfully")
        else:
            print("Invalid Student ID")
    repeat = input("Do you want to continue? (y/n) ")
    return True if repeat.lower() == 'y' else False

