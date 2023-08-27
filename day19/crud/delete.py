import json
filename = "students.json"


def delete_student(student_id):
    with open(filename, "r") as fp:
        students = json.loads(fp.read())
    student = list(filter(lambda x: x["id"] == student_id, students))
    if student:
        students.remove(student[0])
        with open(filename, "w") as fp:
            fp.write(json.dumps(students, indent=2))
        print("Student Has Been Removed !!")
    else:
        print("Invalid Student ID")
    repeat = input("Do you want to continue? (y/n) ")
    return True if repeat.lower() == 'y' else False


