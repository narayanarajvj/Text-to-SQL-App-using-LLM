import sqlite3

## Connect to SQLite
connection=sqlite3.connect("company1.db")

# Create a cursor object to insert record,create table
cursor=connection.cursor()

## Create the table
table_info="""
Create table EMPLOYEE(NAME VARCHAR(25),LEVEL INT,
PRIMARY_SKILL VARCHAR(25),SECONDARY_SKILL VARCHAR(25),
LOCATION VARCHAR(25),GENDER VARCHAR(7));
"""
cursor.execute(table_info)

## Insert some more records
cursor.execute('''Insert Into EMPLOYEE values('Narayan',10,'Python','Prompt','Bangalore','Male')''')
cursor.execute('''Insert Into EMPLOYEE values('Anuruth',11,'Angular','Java','Bangalore','Male')''')
cursor.execute('''Insert Into EMPLOYEE values('Namratha',9,'Prompt','BA','Bangalore','Female')''')
cursor.execute('''Insert Into EMPLOYEE values('Kruthika',10,'SAP','Prompt','Hyderabad','Female')''')
cursor.execute('''Insert Into EMPLOYEE values('Shirisha',11,'Angular','Java','Hyderabad','Female')''')
cursor.execute('''Insert Into EMPLOYEE values('Gireeshma',10,'C#','Python','Hyderabad','Female')''')
# cursor.execute('''Insert Into EMPLOYEE values('Rekha',8,'SAP')''')
# cursor.execute('''Insert Into EMPLOYEE values('Vinay',10,'Prompt')''')
# cursor.execute('''Insert Into EMPLOYEE values('Mathesh',8,'SAP')''')
# cursor.execute('''Insert Into EMPLOYEE values('Shreyas',9,'BA')''')
# cursor.execute('''Insert Into EMPLOYEE values('Sameeran',11,'Testing')''')
# cursor.execute('''Insert Into EMPLOYEE values('Vishal',11,'Backend')''')
# cursor.execute('''Insert Into EMPLOYEE values('Pallavi',9,'Testing')''')
# cursor.execute('''Insert Into EMPLOYEE values('Priyanka',8,'BA')''')

## Display All the records
print("The inserted records are")
data=cursor.execute('''Select * from EMPLOYEE''')
for row in data:
    print(row)

## Commit your changes in the database
connection.commit()
connection.close()