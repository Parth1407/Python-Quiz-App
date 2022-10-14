import mysql.connector as c
con=c.connect(host="localhost",
              user="root",
              passwd="parthpuri",
              database='examportal')
cursor=con.cursor()

try:
    query="create table student(Student_ID varchar(30) primary key,Name varchar(50),Age int,Gender varchar(10),Class int,Password varchar(100))"
    cursor.execute(query)
    con.commit()
    print('Table created successfully!')
except Exception():
    print('Error occured! Try again')
