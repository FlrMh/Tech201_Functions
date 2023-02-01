# Calculator task

# 1st step: add your functions

# Sum function
def addition(num_1: float, num_2: float) -> float:
    return num_1 + num_2

# Minus function
def minus(num_1: float, num_2: float) -> float:
    return num_1 - num_2

# Multiply function
def multiply(num_1: float, num_2: float) -> float:
    return num_1 * num_2

# Divide function
def divide(num_1: float, num_2: float) -> float:
    return num_1 / num_2

# Conversion to m function
def convert(num_3: float) -> float:
    return num_3 * 0.0001



# Building the program

# Asking for choice of operation
operator_choice = input("What calculation would you like to perform? (add, sub, mul, div, conv): ") # this will request for user input in terms of the operation they want to perform

if operator_choice == "conv":
    num_3 = float(input("Please enter the number you want to convert(1st conversion - from cm to m; 2nd conversion - from m to feet):")) # if "conv" is chosen, then the user will be prompted to pick a number to convert from cm to m
    print((convert(num_3)))
    print("meters")
    print(num_3 * 3.2808399)
    print("feet")
else:
    num_1 = float(input("Please, enter the first number: ")) # this will ask for the first choice of number from the user, which will be stored and then used in operations.
    num_2 = float(input("Please, enter the second number: ")) # this will ask for the second choice of number from the user, which will be stored and then used in calculations, alongside the num_1.
    if operator_choice == "add":
        print(addition(num_1, num_2)) # if the user types "add" when prompted to pick an operation, the program will perform the addition operation, based on the addition function we set previously.
    elif operator_choice == "sub":\
        print(minus(num_1, num_2)) # if the user types "sub" when prompted to pick an operation, the program will perform the subtraction operation, based on the minus function we set previously.
    elif operator_choice == "mul":
        print(multiply(num_1, num_2)) # if the user types "mul" when prompted to pick an operation, the program will perform the multiplication operation, based on the multiply function we set previously.
    elif operator_choice == "div":
        print(divide(num_1, num_2)) # if the user types "div" when prompted to pick an operation, the program will perform the division operation, based on the divide function we set previously.
    else:
        print("Sorry, it seems like your input is invalid.") # if the program runs this line, it means that the user introduced a different operator name when asked to provide one from the list prompted.