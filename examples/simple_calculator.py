"""Initial exercise for APPI
"""


def addition(x, y):
    return x + y


def subtraction(x, y):
    return x - y


def division(x, y):
    if y == 0:
        raise ValueError("Cannot divide by 0.")
    return x / y


def multiply(x, y):
    return x * y


supported_operations = ("+", "-", "*", "/")
while True:
    try:
        x = float(input("Enter the first number: "))
        y = float(input("Enter the second number: "))
        operation = input("Select the operation (+ - / *): ")
        if operation not in supported_operations:
            raise ValueError(f"{operation} is not a valid operation.")
        match operation:
            case "+":
                print(addition(x, y))
            case "-":
                print(subtraction(x, y))
            case "*":
                print(multiply(x, y))
            case "/":
                print(division(x, y))
    except ValueError as e:
        print(e)

    if input("Do you want to do another calculation? (yes/no)?: ") == "no":
        break


def addition2(*args):
    result = 0
    for number in args:
        result += number
    return result


# print(addition2(2, 3, 4, 5, 6))
