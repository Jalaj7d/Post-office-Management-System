def adduser():    
    import mysql.connector
    conn=mysql.connector.connect(host="localhost",
                                user='root',
                                passwd="7575",
                                database='project')
    Name=input("Enter the user's name:")
    Pno=int(input('Enter the phone no.:'))
    Pcode=int(input("Enter the postal code:"))
    city=input("Enter the city:")
    date=input("Enter the date of birth:")
    cur=conn.cursor()
    A="insert into user(Name,Pno,Pcode,city,date) values('{0}',{1},{2},'{3}','{4}')".format(Name,Pno,Pcode,city,date)
    cur.execute(A)
    conn.commit()
    print("user details added")
    
def display():
    import mysql.connector
    conn=mysql.connector.connect(host="localhost",
                                user='root',
                                passwd='7575',
                                database='project')
   
    cur=conn.cursor()
    cur.execute("select * from user")
    dis=cur.fetchall()
    print(dis)

def search():
    import mysql.connector
    conn=mysql.connector.connect(host="localhost",
                                 user='root',
                                 passwd='7575',
                                 database='project')
    
    cur=conn.cursor()
    p=input("Enter the postal code to be searched:")
    a="select * from user where Pcode={}".format(p)
    cur.execute(a)
    dis=cur.fetchall()
    print(dis)
    
def modify():
    import mysql.connector
    conn=mysql.connector.connect(host="localhost",
                                user='root',
                                passwd="7575",
                                database='project')
   
    cur=conn.cursor()
    c=0
    while c<=6:
       print("*"*85)
       print("\t\t\t\tUser Details")
       print("*"*85)
       print("\t\t\t\t1.Name")
       print("\t\t\t\t2.Phone")
       print("\t\t\t\t3.Postal code")
       print("\t\t\t\t4.City")
       print("\t\t\t\t5.Date of birth")
       print("\t\t\t\t6.Exit")
       print("*"*85)
       x=int(input("Enter the data to be modified:"))
       print("*"*85)
       if x==1:
          p=input("Enter the present postal code:")
          name=input("Enter the new name:")
          
          a="update user set Name='{}' where Pcode={}".format(name,p)
          cur.execute(a)
          conn.commit()
          print("Name modified!")
          print(cur)
       if x==2:
          p=input("Enter the present postal code:")
          phno=input("Enter the new phone no.:")
          
          a="update user set Pno={} where Pcode={}".format(phno,p)
          cur.execute(a)
          conn.commit()
          print("Phone no. modified!")
          print(cur)
       if x==3:
          p=input("Enter the present postal code:")
          pcode=input("Enter the new postal code:")
          
          a="update user set Pcode={} where Pcode={}".format(pcode,p)
          cur.execute(a)
          conn.commit()
          print("Postal code modified!")
          print(cur)
       if x==4:
          p=input("Enter the present postal code:")
          city=input("Enter the new city:")
          
          a="update user set city='{}' where Pcode={}".format(city,p)
          cur.execute(a)
          conn.commit()
          print("city modified!")
          print(cur)
       if x==5:
          p=input("Enter the present postal code:")
          date=input("Enter the new DOB:")
          
          a="update user set date='{}' where Pcode={}".format(date,p)
          cur.execute(a)
          conn.commit()
          print("DOB modified!")
          print(cur)
       if x==6:
           break
        
def delete():
     import mysql.connector
     conn=mysql.connector.connect(host="localhost",
                                 user='root',
                                 passwd='7575',
                                 database='project')
    
     cur=conn.cursor()
     p=input("Enter the postal code to be deleted:")
     a="delete from user where Pcode={}".format(p)
    
     cur.execute(a)
     conn.commit()
   
     print("data deleted")
     print(cur)

while True:
    print("*"*85)
    print("\t\t\t\tUser Details")
    print("*"*85)
    print("\t\t\t\t1.Add User")
    print("\t\t\t\t2.Display Details")
    print("\t\t\t\t3.Search")
    print("\t\t\t\t4.Modify")
    print("\t\t\t\t5.Delete")
    print("\t\t\t\t6.Exit")
    print("*"*85)

    choice = int(input("Enter your choice: "))
    print("*"*85)

    if choice == 1:
        adduser()
    elif choice == 2:
        display()
    elif choice == 3:
        search()
    elif choice == 4:
        modify()
    elif choice == 5:
        delete()
    elif choice == 6:
        print("Exiting...")
        break
    else:
        print("Invalid entry")

