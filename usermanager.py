from functions import question, add_newuser, find_user, delete_user, lists, authenticate_admin, delete_records

user = {}

if authenticate_admin():
    try:
        while True:
            option = question()

            if option == "i":
                add_newuser(user)

            elif option == "f":
                find_user(user)

            elif option == "d":
                delete_user(user)

            elif option == "l":
                lists(user)

            elif option == "q":
                print("Exiting the system, goodbye!")
                break

            elif option == "x":
                delete_records()

            else:
                print("Invalid option. Please check the correct option and try again")

    except KeyboardInterrupt:
        print("\nProgram interrupted. Exiting gracefully.")
    else:
        print("Authentication failed. Exiting program.")
