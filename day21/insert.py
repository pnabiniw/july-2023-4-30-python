from estd_connection import estd_connection

cursor = estd_connection()

id = input("Enter student ID ")
name = input("Student name ")
age = int(input("Enter student's age "))

sql = f"""
INSERT INTO STUDENT (ID, NAME, AGE) VALUES ('{id}', '{name}', {age})
"""

cursor.execute(sql)
print("Student added successfully !!")
