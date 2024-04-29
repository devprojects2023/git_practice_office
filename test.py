# This is a simple user_input function
name = ["Dev", "Avik", "Raj"]
def myname():
    if user_input in name:
        print("Available")
    else:
        name.append(user_input)
        print(f"{user_input} is added in the list")
        print(name)

user_input = input("Enter your name: \n")
myname()
