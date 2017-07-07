#CRUD Operations on database using sql connector

import MySQLdb

#Connect database
db=MySQLdb.connect("localhost","root","1234","testdb")

#Get cursor pointer
cursor=db.cursor();

#Generate SQL Query
sql="""
INSERT INTO EMPLOYEES VALUES (1,'ALEX',3344.32),(2,'JOHN',1224.62)
"""

#Execute SQL Query
try:
    #Execute sql query
    cursor.execute(sql)
    #Commit changes to database
    db.commit()
except:
    #Rollback the execution if any exception occurred
    db.rollback()



#Reading the data from table
sql="""
SELECT * FROM EMPLOYEES WHERE SALARY>2000
"""
try:
    #Execute sql query
    cursor.execute(sql)
    #Fetch all records from the executed query result set
    records=cursor.fetchall()
    #Iterate through the result set
    for row in records:
        print("Name:{},Salary:{}".format(row[1],row[2]))

except:
    print("Unable to fetch records")


#Updating data
sql="""
UPDATE EMPLOYEES
SET SALARY=SALARY+500
WHERE SALARY<2000
"""

try:
    #Execute SQL Query
    cursor.execute(sql)
    #Commit changes to database
    db.commit();
    print("Salaries Updated")
except:
    #Roll back incase of failure
    db.rollback()



#Deleting the records from table
sql="""
DELETE FROM EMPLOYEES WHERE NAME LIKE '%JOHN%'
"""

try:
    #Execute sql query
    cursor.execute(sql)
    print("John-ish employees are FIRED !!!!")
    #Commit changes to database
    db.commit()

except:
    #Roll back incase of any error
    db.rollback()

#Close db connection
db.close()




