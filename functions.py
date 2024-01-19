import os
#This function deletes records in the saveLogs.txt file based on the login provided by the user.
#The code first checks that the file exists (os.path.exists(filename)).
#It reads all the lines in the file and asks for the login to be deleted.
#Rewrites all the lines in the file that do not contain the login provided.
#Informs if the deletion was successful or if the file was not found.
def delete_records():
    filename = "saveLogs.txt"
    if os.path.exists(filename):
        with open(filename, "r") as file:
            lines = file.readlines()

        login_to_delete = input("Enter the login to delete records: ").upper()

        with open(filename, "w") as file:
            for line in lines:
                if login_to_delete not in line:
                    file.write(line)

        print("Records delete sucessfully! ")
    else:
        print("File not found!")

# here I've created a function called questioning, basically I'm going to ask for the new user's data
        #so I used this < > structure to represent an action in my system, using these little letters
        #<i> it will be to insert a new user
        #<f>it will be to search for users in the system
        #<d> will be to delete the user
        #<l> will be to list all users within the system
        #<q> it will be to get out of the system
        #<x> to delete user information or records

def question():
    return input("What do you want to do now?\n"
        "<i> - To add a new user in the system\n" +
        "<f> - To find a user in the system\n" +
        "<d> - To delete a user in the system\n" + 
        "<l> - To list users in the system\n"
        "<q> - To quit\n"
        "<x> - To delete records in saveLogs\n").lower()

# as in the insert <i> command I'm going to add a user, so I created a def to do this
    # define that this function will create the user, and will be responsible for asking for registration data such as name, login, gmail, password, when was the first access ie accessed before
        # I used the dictionary structure to store all these questions!
    # and at the end of the registration, if all goes well, it will add it correctly, and it will print the message user added successfully!
def add_newuser(dictionary):
    dictionary[input("Type in the new user's login: ").upper()] = [input("Type in the name of the new user: ").upper(), 
    input("When will your first access be? "), input("Which host the user accessed: ") ,
    input("What will the new user's password be?: "), input("What is the user's level?"), input("What`s your gmail :") ]
    print("User added successfully!")
    
    save_datas(dictionary)
# ready, this saveDatas will be where the add_newuser logs will be saved, when a new user is added to the system, it will go to a txt file, where
    # all the information will appear!
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
# here is where we will look for the user, let's say there are 200 employees registered, this function will look for the user by login.
def delete_user(users):
    login_to_delete = str(input("Enter the login to delete: ")).upper() 
    if login_to_delete in users:
        del users[login_to_delete]
        print("User deleted successfully!")
    else:
        print("User not found to be deleted")
#this is the option to delete the user, the function del = delete , if the system does not find the login, it says user not found to be deleted!
def lists(users):
    print("Lists of users registered in the system: ")
    for login, info in users.items():
        print("Login: ", login)
        print("Name: ", info[0])
        print("Last Date of Access: ", info[1])
        print("Department Access: ", info[2])
    print("--------------------------------------------")
    print()
#this is our list of users, when the user presses l, it will list them in the vscode terminal!
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
#I created this function to be more of a protection measure, let's say you have access to this code, it will have to go through admin authentication   

#let`s create more functionn!!!!!!!!!!!!!!!!`
def save_datas(dictionary):
    with open("saveLogs.txt", "a") as file:
        for keys,values in dictionary.items():
            file.write(keys + ":" + str(values))
# here is where the logs will be redirected, when save_datas is done in add_newuser, all the logs will go to this SaveLogs.txt
