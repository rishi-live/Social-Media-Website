import mysql.connector

#connect to the database
conn=mysql.connector.connect(host="localhost", user="root", password="", database="UEMK" )
mycursor=conn.cursor()

def user_menu():
    user_input=input("""What would you like to do?
    1. Enter 1 to insert :
    2. Enter 2 to see all users :
    3. Enter 3 to update the user's imfo :
    4. Enter 4 to delete the user :""")

    if user_input=="1":
        #insert
        insert()
    elif user_input=="2":
        #read
        read()
    elif user_input=="3":
        #update
        update()
    else:
        #delete
        delete()


def insert():
    print("Insert")
    name=input("Enter name of the new user :")
    email=input("Enter email of the new user :")
    password=input("Enter password of new user :")

    mycursor.execute("""
    INSERT INTO `users` (`user_id`, `name`, `email`, `password`) VALUES 
    (NULL, '{}', '{}', '{}')
    """.format(name, email, password))
    # {} using for string formatting for user input
    conn.commit()

    print("Insertion successful")
    user_menu()

def read():
    print("Read")

    mycursor.execute("""
    SELECT * FROM `users`
    """)

    user_details=mycursor.fetchall()
    # print tuples  and not showing password
    #  in we can not change any thing tuple
    for i in user_details:
        print(i[1],"|",i[2])
        print("---------------------")

def update():

    email=input("Enter the email of the user whose info you would like to change :")
    name=input("Enter new name :")
    password=input("Enter new password :")

    mycursor.execute("""
    UPDATE `users` SET `name`='{}', `password`='{}' WHERE `email` LIKE '{}'
    """.format(name, password, email))

    conn.commit()

    print("Update successful")

    user_menu()

def delete():
    print("Delete")
    email=input("Enter the email id of the user to be deleted :")

    mycursor.execute("""
    DELETE FROM `users` WHERE `email` LIKE '{}'
    """.format(email))

    conn.commit()

    print("Deletion successful")
    user_menu()



user_menu()