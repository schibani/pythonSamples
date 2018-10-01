def add(num1, num2):
    """Returns num1 plus num2"""
    return num1 + num2


def sub(num1, num2):
    """Returns num1 minus num2"""
    return num1 - num2


def mul(num1, num2):
    """Returns num1 multiply num2"""
    return num1 * num2


def div(num1, num2):
    """Returns num1 divide num2"""
    return num1 / num2


def runOperation(operation, num1, num2):
    """Determine the operation to run based on the operation argument which should be passed in as an int."""
    # Determine the operation to apply
    if operation == 1 or operation == '+':
        print("Adding...")
        print(add(num1, num2))
    elif operation == 2 or operation == '-':
        print("Subtracting...")
        print(sub(num1, num2))
    elif operation == 3 or operation == '*':
        print("Multiplying...")
        print(mul(num1, num2))
    elif operation == 4 or operation == '/':
        print("Dividing...")
        print(div(num1, num2))
    else:
        print("I don't understand what do you want to do")


def main():
    """Allows user to run basic calculator operations with two numbers """
    validInput = False
    while not validInput:
        # Get user input
        try:
            num1 = int(input("What is number 1?"))
            num2 = int(input("What is number 2?"))
            operation = int(input("What do you want to do? 1. add, 2. subtract, 3. multiply, or 4. divide."
                                  " Enter  number: "))
            validInput = True
        except ValueError:
            print("Invalid input. Try again.")
        except:
            print("Unknown error")
        run_operation(operation, num1, num2)


if __name__ == "__main__":
    main()
