print("=")
print("Login Page")
print("="*'#')

username = input("Username: ")
password = input("Password: ")

while username == "user098":
    try:
        if password == "pass098":
            print("Welcome User: {}".format(username))
        elif password != "pass098":
            print("invalid password, try again")
        except