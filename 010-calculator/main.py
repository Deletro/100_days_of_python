# calculator functions
# Add


def add(n1, n2):
    print(f"Result: {n1+n2}")


# Subtract


def subtract(n1, n2):
    print(f"Result: {n1-n2}")


# Multiply


def multiply(n1, n2):
    print(f"Result: {n1*n2}")


# Divide


def divide(n1, n2):
    print(f"Result: {n1/n2}")


# dict what contains the functions and the operators

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}


keep_going = "yes"


while keep_going == "yes":
    num1 = int(input("First number:\n"))
    function = operations[input("Choose the operation:\n'+', '-', '*', '/':\n")]
    num2 = int(input("Second number:\n"))
    function(n1=num1, n2=num2)
    loop_breaker = input("Do you want to continue?:\n 'yes', 'no':\n")
    if loop_breaker == "yes":
        continue
    else:
        keep_going = loop_breaker
        print("Goodbye")
