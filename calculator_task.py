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


# Asking for user input

num_1 = float(input("Please, enter the first number: ")) # this will ask for the first choice of number from the user, which will be stored and then used in operations.
num_2 = float(input("Please, enter the second number: ")) # this will ask for the second choice of number from the user, which will be stored and then used in calculations, alongside the num1.
# requesting the numbers` input before asking for the operator choice ensures that we establish values for the numbers that the user wants to perform calculations with.

# Building the program

# Ask the user for the preferred operator
operator_choice = input("What calculation would you like to perform? (add, sub, mul, div): ") # this will be printed after num1 and num2 have been chosen, so we can now perform the functions, depending on the user`s operator choice.
if operator_choice == "add":
    print(addition(num_1, num_2)) # if the user types "add" when prompted to pick an operation, the program will perform the addition operation, based on the addition function we set previously.
elif operator_choice == "sub":
    print(minus(num_1, num_2)) # if the user types "sub" when prompted to pick an operation, the program will perform the subtraction operation, based on the minus function we set previously.
elif operator_choice == "mul":
    print(multiply(num_1, num_2)) # if the user types "mul" when prompted to pick an operation, the program will perform the multiplication operation, based on the multiply function we set previously.
elif operator_choice == "div":
    print(divide(num_1, num_2)) # if the user types "div" when prompted to pick an operation, the program will perform the division operation, based on the divide function we set previously.
else:
    print("Sorry, it seems like your input is invalid.") # if the program runs this line, it means that the user introduced a different operator name when asked to provide one from the list prompted.