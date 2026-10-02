user = input("Enter username: ")
password = input("Enter password: ")
if user == "admin" and password == "admin123":
    role = "Administrator"
    
    if role == "Administrator":
        print(f"Role: {role}")
        print(f"Full system access")
elif user == "student12" and password == "study123":
    role = "Student"
    
    if role == "Student":
        print(f"Role: {role}")
        print(f"Student access")
else:
    print(f"Invalid username or password")