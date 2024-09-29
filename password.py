import random
password= input("Input master password: ")
def add():
    name=input("Enter account Name: ")
    pwd =input("Enter Password: ")
    with open("passwords.txt","a") as f:
     f.write(name+"|"+"pwd")   
        
if password == "faith":
        print("welcome Faith!!")
        add()
        
else:
        print("invalid")
        quit()