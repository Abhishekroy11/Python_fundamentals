username = input("Enter username: ")
password = input("Enter password: ")

if(username == "Admin" and password == "Abhishek"):
    print("Succesfull Login...")
else:
    if(username != "Admin"):
        print("Wrong Username Entered...")
    else:
        print("Wrong password Entered...")