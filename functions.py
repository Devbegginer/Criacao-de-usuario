def question():
    return input("What do you want to do now?\n"
        "<i> - To add a new user in the system\n" +
        "<f> - To find a user in the system\n" +
        "<d> - To delete a user in the system\n" + 
        "<l> - To list users in the system\n"
        "<q> - To quit\n").lower()

def add_newuser(dictionary):
    dictionary[input("Type in the new user's login: ").upper()] = [input("Type in the name of the new user: ").upper(), 
    input("When will your first access be? "), input("Which host the user accessed: ") ,
    input("What will the new user's password be?: "), input("What is the user's level?"), input("What`s your gmail :") ]
    print("User added successfully!")
    
def find_user(users):
    login_to_find = str(input("Enter with your login: ")).upper()
    if login_to_find in users:
        print("user found: ")
        print("Login: ", login_to_find)
        print("Name:", users[login_to_find][0])
        print("Last date of access: ", users[login_to_find][1])
        print("Department Access:  ", users[login_to_find][2])
    else:   
        print("User not found.")
    
def delete_user(users):
    login_to_delete = str(input("Enter the login to delete: ")).upper() 
    if login_to_delete in users:
        del users[login_to_delete]
        print("User deleted successfully!")
    else:
        print("User not found to be deleted")

def lists(users):
    print("Lists of users registered in the system: ")
    for login, info in users.items():
        print("Login: ", login)
        print("Name: ", info[0])
        print("Last Date of Access: ", info[1])
        print("Department Access: ", info[2])
    print("--------------------------------------------")
    print()

def lists(users):
    print("--------------------------------------------")
    print("lists of users registered in the system  : ")
    for login, info in users.items():
        print("Login: ", login)
        print("Name : ", info[0])
        print("last Date of Acess: ", info[1])
        print("Departament Acess: ", info[2])
    print("--------------------------------------------")

def authenticate_admin():
    admin_username = "admin"
    admin_password = "admin123"
    entered_username = input("Enter admin username: ")
    entered_password = input("Enter admin password: ")
    if entered_username == admin_username and entered_password == admin_password:
        print("Authenticate sucessful. Acess Granted")
        return True
    else:
        print("Authenticate failed. Acess Denied")
        return False

