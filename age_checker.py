age = int(input("Enter the age:  "))
if age >= 18:
    print("Adult")
elif ( age >= 13 and age < 18):
    print("Teenager")
else:
    print("Child")