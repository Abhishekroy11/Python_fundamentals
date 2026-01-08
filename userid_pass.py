# userid_pass.py
username = input("Enter username: ")
password = input("Enter password: ")
if (username == "Abhishek" and password == "1234"):
    print("Login Successful")
elif(username != "Abhishek"):
    print("Invalid Username")
else:
    print("Invalid Password")