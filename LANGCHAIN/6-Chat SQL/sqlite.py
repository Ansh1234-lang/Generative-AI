import sqlite3

## connect to sqllite
connection = sqlite3.connect("student.db")

## create a cursor object to insert record,create table
cursor = connection.cursor()

## create the table if it doesn't exist
table_info = """
CREATE TABLE IF NOT EXISTS STUDENT(
    NAME VARCHAR(25),
    CLASS VARCHAR(25),
    SECTION VARCHAR(25),
    MARKS INT
)
"""
cursor.execute(table_info)

## Optional: Clear table before inserting new records
cursor.execute("DELETE FROM STUDENT")

## Insert some more records
cursor.execute("INSERT INTO STUDENT VALUES('Ansh','Data Science','A',90)")
cursor.execute("INSERT INTO STUDENT VALUES('John','Data Science','B',100)")
cursor.execute("INSERT INTO STUDENT VALUES('Bob','Data Science','A',86)")
cursor.execute("INSERT INTO STUDENT VALUES('Jacob','DEVOPS','A',50)")
cursor.execute("INSERT INTO STUDENT VALUES('Dipesh','DEVOPS','A',35)")

## Display all the records
print("The inserted records are")
data = cursor.execute("SELECT * FROM STUDENT")
for row in data:
    print(row)

## Commit your changes in the database
connection.commit()
connection.close()
