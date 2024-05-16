from os import system
import time, sqlite3
# Time Clock(start)
start = time.time()

connection=sqlite3.connect('database.db')
cursor=connection.cursor()
print('Welcome to Aashir DataBase.....')
a='yes'
while(a.lower()=='yes' or a.lower()=='y'):
    opt=int(input(' [1]Create Table\n [2]Data Entry\n [3]Delete Table \n ==> '))
    if(opt==1):
        sql_command="""CREATE TABLE student(
        Admno INTEGER PRIMARY KEY,
        Name VARCHAR(50) NOT NULL,
        Gender CHAR(6),
        Age INTEGER(2) DEFAULT '16',
        Class CHAR(7) NOT NULL,
        Address VARCHAR(50),
        Phone_number INTEGER NOT NULL UNIQUE);"""
        cursor.execute(sql_command)
        print('Table Sucessfully Created.....')
        continue
    elif(opt==2):
        sql_command="""INSERT INTO student(Admno,Name,Gender,Class,Phone_number) VALUES(NULL,'{}','{}','{}',{});"""
        for j in range(int(input('Enter the Number of Data: '))):
            cursor.execute(sql_command.format(input('Enter the Name: '),input('Enter the Gender: '),input('Enter the Class: '),int(input('Enter the Phone_number: '))))
            system('clear')
        sql_command="""SELECT * FROM student;"""
        cursor.execute(sql_command)
        print('Inputed data')
        for i in cursor.fetchall():
            print(i)
    elif(opt==3):
        sql_command="""DROP TABLE student;"""
        cursor.execute(sql_command)
        print('Table Sucessfully Deleted.....')
    else:
        print('ERROR!!!Enter correct Option.....')
    a=input('\nDo you want to continue?.....[Yes/NO]: ')
connection.commit()
connection.close()


# Time Clock(end)
end = time.time()
# Time elapsed(start-end)
seconds = end - start
# clear screen
# system('cls')
# system('clear')
# Print time executed
print('Execution time: {0:.03f} s'.format(seconds))
# input('Press ENTER to continue......')
# exit()
