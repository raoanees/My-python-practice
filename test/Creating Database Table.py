import MySQLdb

#Open connection for database
db = MySQLdb.connect("localhost","root","1234","testdb")

cursor = db.cursor()
cursor.execute("DROP TABLE IF EXISTS EMPLOYEES")

#Create database table using SQL query
sql = """CREATE TABLE EMPLOYEES
        (ID INT PRIMARY KEY,
         NAME NVARCHAR(20) NOT NULL ,
         SALARY FLOAT NOT NULL 
         )
        """

#Execute SQL Query
cursor.execute(sql)

#Close database connection
db.close()

