import sqlite3

connection = sqlite3.connect('mydata.db')
cursor = connection.cursor()

cursor.execute("""
    Create Table If Not Exists Persons (
        first_name Text, 
        last_name Text, 
        age INTEGER
    )
""")

cursor.execute("""
    Insert Into Persons Values
    ('Arham', 'Amir', 22),
    ('Ameer', 'Hamza', 28),
    ('Saad', 'Gilani', 26)
""")

cursor.execute("""
    Select * from Persons
""")

print(cursor.fetchall())

connection.commit()
connection.close()