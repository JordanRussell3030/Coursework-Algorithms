import random

usernames = []
passwords = []
logins = []

character_list = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

def generate_usernames():
    with open("user_names.txt", mode = "r") as user_names:
        for name in user_names:
            username = name
            usernames.append(username)

def generate_password(usernames):
    for username in usernames:
        password1 = random.choice(character_list)
        password2 = random.choice(character_list)
        password3 = random.choice(character_list)
        password4 = random.choice(character_list)
        password5 = random.randint(1, 9)
        password6 = random.randint(1, 9)
        password7 = random.randint(1, 9)
        password = password1 + str(password5) + password2 + str(password6) + password3 + str(password7) + password4
        passwords.append(password)
    return passwords

def combine_username_password(usernames, passwords):
    ucount = 0
    pcount = 0
    for username in usernames:
        login = usernames[ucount] + passwords[pcount]
        logins.append(login)
        ucount += 1
        pcount += 1
    return logins

def save_logins(logins):
    with open("logins.txt", mode = "w") as logins_:
        for login in logins:
            logins_.write(login)
            logins_.write("\n")

if __name__ == "__main__":
    username = generate_usernames()
    password = generate_password(usernames)
    login = combine_username_password(usernames, passwords)
    print(usernames)
    print(passwords)
    print(logins)
    save_logins(logins)

    
