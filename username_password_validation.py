list_ = []
with open("logins.txt", mode = "r") as logins:
    for name in logins:
        list_.append(name)
    print(list_)

def input_username(list_):
    username = input("Please enter your username: ")
    return username

def input_password(list_):
    password = input("Please input your password: ")
    return password

def validate(username, password, list_):
    found = False
    count = 0
    while found == False and count < len(list_):
        if str(list_[count]) == username and str(list_[count + 1]) == password:
                print("Accepted")
                found = True
                return found
        else:
            print("Not accepted")
            validation()
        count = count + 1
                
def validation():
    username = input_username(list_)
    password = input_password(list_)
    validate(username, password, list_)

if __name__ == "__main__":
    validation()
    
