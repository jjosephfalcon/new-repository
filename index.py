
users = {}       
vaults = {}      


def sign_up():
    username = input("choose a username: ")

    if username in users:
        print("that username is already taken")
        return

    password = input("choose a master password: ")
    users[username] = password
    vaults[username] = []
    print("account created! you can now login")


def login():
    username = input("username: ")
    password = input("password: ")

    if username in users and users[username] == password:
        print(f"welcome back, {username}!")
        vault_menu(username)
    else:
        print("wrong username or password")


def vault_menu(username):
    while True:
        print("--------------------")
        print("1. Add a password")
        print("2. View my passwords")
        print("3. Logout")

        choice = input("choose: ")

        if choice == "1":
            website = input("website: ")
            account_username = input("account username: ")
            account_password = input("account password: ")
            category = input("category: ")

            vaults[username].append({
                "website": website,
                "username": account_username,
                "password": account_password,
                "category": category,
            })
            print("saved!")

        elif choice == "2":
            saved = vaults[username]

            if not saved:
                print("no saved passwords yet")
            else:
                for entry in saved:
                    print(entry["website"], "-", entry["username"], "-", entry["password"], "-", entry["category"])

        elif choice == "3":
            print("logged out")
            break
        else:
            print("Invalid choice")


while True:

    print("====================")
    print("       Vault X         ")
    print("====================")
    print("1. Sign Up")
    print("2. Login")
    print("3. Exit")

    choice = input("choose: ")

    if choice == "1":
        sign_up()
    elif choice == "2":
        login()
    elif choice == "3":
        print("Exit")
        print("goodbye")
        break
    else:
        print("Invalid choice")