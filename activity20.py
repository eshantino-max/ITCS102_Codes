#water = 10
#while water > 0:
## water -= 1


from getpass import getpass
login = False
while login == False:
    username = input("Enter your username: ")
    password = getpass("Enter your password: ")
    if username == "shantino" and password == "password":
        print("Login successful!")
        login = True
    else:
        print("Invalid username or password. Please try again.")