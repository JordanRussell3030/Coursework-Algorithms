class_ = []

def get_name():
    name = str(input("Please enter the name of the user you would like to add: "))
    class_.append(name)
    add_another()

def add_another():
    exit_ = input("Would you like to add another user? (Y/N) ")
    if exit_.upper() == "Y":
        get_name()
    elif exit_.upper() == "N":
        save_names()
    elif exit_.upper() == "L":
        print(class_)
        add_another()
    else:
        print("Please enter a valid value")
        add_another()

def save_names():
    with open("user_names.txt", mode = "w") as user_names:
        for name in class_:
            user_names.write(name)
            user_names.write("\n")

if __name__ == "__main__":
    get_name()
    
    

