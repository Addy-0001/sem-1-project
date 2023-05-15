import sqlite3

connection = sqlite3.connect("company.db")
print("Opened Database Successfully")

connection.execute('''CREATE TABLE COMPANY
    (ID INT PRIMARY KEY NOT NULL,
    NAME TEXT NOT NULL,
    AGE INT NOT NULL, 
    ADDRESS CHAR(100),
    SALARY REAL);''')
print("Table created successfully")

connection.execute("INSERT INTO  COMPANY(ID, NAME, AGE, ADDRESS, SALARY) \
    VALUES (1, 'ADAMYA', 21, 'NEPAL', 30000.00)")

connection.commit()

print("Records created successfully")

print("Exporting data from the database")

cursor = connection.execute(
    "SELECT ID, NAME, AGE, ADDRESS, SALARY FROM COMPANY")
for row in cursor:
    print("ID = ", row[0])
    print("NAME = ", row[1])
    print("AGE = ", row[2])
    print("ADDRESS = ", row[3])
    print("SALARY = ", row[4], "\n")
print("Pring Operation completed Successfully")

# changing the data using UPDATE in the database
connection.execute("UPDATE COMPANY set SALARY = 50000.00 where ID = 1")
connection.commit()

cursor = connection.execute(
    "SELECT ID, NAME, AGE, ADDRESS, SALARY FROM COMPANY")
for row in cursor:
    print("ID = ", row[0])
    print("NAME = ", row[1])
    print("AGE = ", row[2])
    print("ADDRESS = ", row[3])
    print("SALARY = ", row[4], "\n")
print("Print Operation completed Successfully")

connection.close()
