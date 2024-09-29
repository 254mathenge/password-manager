import random

password = input("Input master password: ")


def add():
    name = input("Enter account Name: ")
    pwd = input("Enter Password: ")
    with open("passwords.txt", "a") as f:
        f.write(name + "|" + pwd + "\n")


def view():
    with open("passwords.txt","r") as f:
        for line in f.readlines():
            print(line.rstrip())

if password == "faith":
    print("welcome Faith!!")
    view_add = input("Would you like to add a new password or view existing ones(view,add),press q to quit? ")
    if view_add == "add":
        add()
    elif view_add == "view":
        view()
    elif view_add == "q":
        quit()
    else:
        print("Invalid input")
else:
    print("invalid")
    quit()
