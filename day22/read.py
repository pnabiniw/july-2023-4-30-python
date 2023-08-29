from day21.estd_connection import estd_connection

cursor = estd_connection()


def read_student(student_id):
    sql = f"""
    SELECT * FROM STUDENT WHERE ID='{student_id}'
    """
    cursor.execute(sql)
    result = cursor.fetchone()
    print(result)
    repeat = input("Do you want to continue? (y/n) ")
    return True if repeat.lower() == 'y' else False
