# Goal:
# Create a calculator program. It should:
# - print an introduction message
# - take input from the user
# - perform addition, subtraction, multiplication and division
# - print the calculation it performs AND the result

def _introduction(operation):
    welcome_string = "Welcome to the calculator program."
    prompt_string = f"Please give me two values to {operation}"
    print(f"{welcome_string}\n{prompt_string}")

def _get_number(index):
    number = float(input(f"Number {index}: "))
    return number

def _print_result(first, second, operation, result):
    print(f"{first} {operation} {second} = {result}")

# ------------------------------- #

def add_numbers():
    _introduction("add")
    num1 = _get_number(1)
    num2 = _get_number(2)
    result = num1 + num2
    _print_result(num1, num2, "+", result)

def subtract_numbers():
    _introduction("subtract")
    num1 = _get_number(1)
    num2 = _get_number(2)
    result = num1 - num2
    _print_result(num1, num2, "-", result)

def multiply_numbers():
    _introduction("mutilply")
    num1 = _get_number(1)
    num2 = _get_number(2)
    result = num1 * num2
    _print_result(num1, num2, "*", result)

def divide_numbers():
    _introduction("divide")
    num1 = _get_number(1)
    num2 = _get_number(2)
    result = num1 / num2
    _print_result(num1, num2, "/", result)

