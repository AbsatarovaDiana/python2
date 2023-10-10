import re
db = {"Ali": "ali", "Akbota": "2003", "Erasyl": "Era2010"}

  
def show_db():
    print(db)


def chang_name(old_name, new_name, password):
    while password != db[old_name]:
        password = input("Wrong password! Try again: ")

    db[new_name] = db[old_name]
    del db[old_name]


def add_user(name, password):
    if name not in db.keys():
        db[name] = password
        print("New dictionary:",db)
    else:
         name = input("Plz choose another name: ")
         db[name] = password
         print("New dictionary:",db)

    if check_password(password) == True:
        db[name] = password


def check_password(password):
    match = re.fullmatch(r'[A-Za-z0-9@#$%^&+=]{8,}', password)
    if match:
        print("the good one")
    else:
         password = input("Enter another password: ")

    return True


def change_password(name, old_password, new_password):
    while old_password != db[name]:
        old_password = input("Wrong password! Try again: ")
    if re.fullmatch(r'[A-Za-z0-9@#$%^&+=]{8,}', new_password):
        db.update({name: new_password})
    else:
         new_password = input("Wrong password! Try again: ")


print("Welcome to the users database!")
action = input(
    "What would you like to do? show db/add User/change Name/change Password/quit: "
)

if action == "quit":
        print("Okay, the session is over. Bye!")
if action == "show db":
        show_db()
elif action == "add User":
        name = input("Enter name: ")
        password = input("enter password: ")
        add_user(name, password)
        print("Done!")
elif action == "change Name":
        old_name = input("Enter old name: ")
        new_name = input("Enter new name: ")
        password = input("Enter password: ")
        chang_name(old_name, new_name, password)
        print("Done!")
elif action == "change Password":
        name = input("Enter your name: ")
        old_password = input("Enter old password: ")
        new_password = input("Enter new password: ")
        change_password(name, old_password, new_password)
        print("Done!")
else: 
        action = input(
            f"""There is no such action as \"{action}\". \nPossible action: show db/add User/change Name/change Password/quit \nTry again: """
        )





