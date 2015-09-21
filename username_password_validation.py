list_ = []
with open("logins.txt", mode = "r") as logins:
    for name in logins:
        list_.append(name)
    print(list_)
    print(list_[0])
    print(list_[1])
    print(list_[2])
    print(list_[3])
    print(list_[4])
    print(list_[5])

def input_username(list_):
    username = input("Please enter your username: ")
    return username

def input_password(list_):
    password = input("Please input your password: ")
    return password

def validate(username, password, list_):
    count = 0
    found = False
    while found == False and count < len(list_):
        if list_[count] == str(username) and list_[count + 2] == str(password):
            print("Accepted")
            found = True
            return found
        else:
            print("Not accepted")
            print(list_[count])
            print(list_[count + 2])
            validation()
        count = count + 1
                
def validation():
    username = input_username(list_)
    password = input_password(list_)
    validate(username, password, list_)

if __name__ == "__main__":
    validation()
    
