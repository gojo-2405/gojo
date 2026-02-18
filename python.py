user={
    "karthick":"admin",
    "admin":"admin",
    }
operation=input("signup/login: ")
if operation=="signup":
    new_user=input("username: ")
    new_pass=input("password: ")
    if new_user in user:
        print("user already exist")
    else:
        user[new_user]=new_pass
        print("successfully signed up")
elif operation=="login":
    usern=input("username: ")
    passwd=input("password: ")
    if usern in user and user[usern]==passwd:
        if usern=="karthick":
            print("logged in as karthick")
        elif usern=="admin":
            print("logged in as admin")
        else:
            print(f"logged in as {usern}")
    else:
        print("invalid credentials")
else:
    print("invalid operation")
        
            
