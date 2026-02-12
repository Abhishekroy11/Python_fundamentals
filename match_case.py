color = input("Enter the color:- ")
match color:
    case "Green":
        print("Go")
    case "Yellow":
        print("Ready")
    case "Red":
        print("Stop")
    case _:
        print("Invalid traffic signal color....")