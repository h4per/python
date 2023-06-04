import sqlite3

def create_connection(db_name):
    connection = sqlite3.connect(db_name)
    return connection


def create_table(conn, sql):
    cursor = conn.cursor()
    cursor.execute(sql)


student = (1, "Islam", None, None, "2006-12-16")
def create_students(conn, student: tuple):
    sql = '''INSERT INTO students 
    (full_name, marks, hobby, birth_date) 
    VALUES (?, ?, ?, ?);'''
    cursor = conn.cursor()
    cursor.execute(sql, student)
    conn.commit()


def delete_student(conn, id:int):
    sql = '''DELETE FROM students WHERE id = ?;'''
    cursor = conn.cursor()
    cursor.execute(sql, (id,))
    conn.commit()


def update_student_marks(conn, id:int, new_mark):
    sql = '''UPDATE students SET marks = ? WHERE id = ?;'''
    cursor = conn.cursor()
    cursor.execute(sql, (new_mark, id,))
    conn.commit()


def select_students(conn):
    sql = '''SELECT * FROM students;'''
    cursor = conn.cursor()
    rows = cursor.execute(sql).fetchall()
    for row in rows:
        print(row)


sql_create_table = '''
CREATE TABLE IF NOT EXISTS students (
id INTEGER PRIMARY KEY AUTOINCREMENT, 
full_name VARCHAR (200) NOT NULL,
marks DOUBLE (5, 2) DEFAULT 0.0,
hobby TEXT DEFAULT NULL,
birth_date DATE NOT NULL
);
'''

connection = create_connection("oleg.db")
if connection:
    print("База данных подключена")
    # create_table(connection, sql_create_table)
    # create_students(connection, ("Islam", 25.6, None, "2006-12-16"))
    # delete_student(connection, 2)
    # update_student_marks(connection, 3 , 100.0)
    # select_students(connection)
