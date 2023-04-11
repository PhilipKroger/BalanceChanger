f = open("database.txt", "r")
s = f.readlines()
f.close()

# from file to dictionary
base_dict = {}
for i in range(len(s)):
    k = str(s[i].split()[0])
    v = int(s[i].split()[1])
    base_dict[k] = v

print("Our dictionary with names and balances")
print(base_dict)

print("Enter sender's name, recipient's name and transfer amount (Example) Max Vlad 20")
user_input = input("Enter: ")


def bank(user_input):
    if len(user_input.split()) == 3:
        user_1 = str(user_input.split()[0])  # sender
        user_2 = str(user_input.split()[1])  # recipient
        amount = int(user_input.split()[2])  # amount

        """Our sender and recipient are in the dictionary 'base_dict' """
        if amount <= base_dict[user_1]:
            if user_1 in base_dict.keys() and user_2 in base_dict.keys():
                base_dict[user_2] += amount  # recipient get his money
                base_dict[user_1] -= amount  # sender gave his money
                f_1 = open('database.txt', 'w')
                l = 0
                """ Search for the maximum length key """
                for key, value in base_dict.items():
                    if len(key) > l:
                        l = len(key)

                """ Enter new data to the file 'database.txt' """
                for key, value in base_dict.items():
                    f_1.write("{0}".format(key) + " {0} \n".format(value))

                return "Operation was successfully"
            else:
                return "UserDoesNotExist or The"
        else:
            return "There is not enough money on the balance sheet"
    else:
        return "IncorrectInputError"


def delete_user(user_input):
    """Command: delete user. Example: delete Maks."""
    username = str(user_input.split()[1])
    f_1 = open('database.txt', 'w')
    for key, value in base_dict.items():
        f_1.write("{0}".format(key) + " {0} \n".format(value))
    del base_dict[username]
    return "Operation was successfully"


def add_user(user_input):
    """Command: add user. Example: add Maks. Default balance = 0."""
    username = str(user_input.split()[1])
    base_dict[username] = 0
    return "Operation was successfully"


if str(user_input.split()[0]) == 'bank':
    print(bank(user_input))
elif str(user_input.split()[0]) == 'delete':
    print(delete_user(user_input))
elif str(user_input.split()[0]) == 'add':
    print(add_user(user_input))
else:
    print('Incorrect input')

print(base_dict)
