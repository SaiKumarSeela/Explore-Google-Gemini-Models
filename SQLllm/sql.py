import sqlite3

connection = sqlite3.connect("student.db")

cursor = connection.cursor()

table_info = """
Create table STUDENT(NAME VARCHAR(25), CLASS VARCHAR(25),
SECTION VARCHAR(25), MARKS INT);
"""

cursor.execute(table_info)

# insert records

cursor.execute('''Insert Into STUDENT values('Saikumar','CSM','A',90)''')
cursor.execute('''Insert Into STUDENT values('Priestly','CSM','B',100)''')
cursor.execute('''Insert Into STUDENT values('KVR','CSM','A',86)''')
cursor.execute('''Insert Into STUDENT values('Naveen','ECE','A',50)''')
cursor.execute('''Insert Into STUDENT values('Suresh','ECE','A',35)''')

# Display all the records
print("The inserted records are")

data = cursor.execute('''Select * from STUDENT''')

for row in data:
    print(row)


connection.commit()
connection.close()


