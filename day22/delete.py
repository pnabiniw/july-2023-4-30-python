from day21.estd_connection import estd_connection

cursor = estd_connection()

def delete_student(student_id):
    sql = f"""
    DELETE FROM STUDENT WHERE ID='{student_id}'
    """

    cursor.execute(sql)
    print("Student Has Been Removed !!")
    repeat = input("Do you want to continue? (y/n) ")
    return True if repeat.lower() == 'y' else False


