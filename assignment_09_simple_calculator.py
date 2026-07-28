# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 9
# =============================================================================
#
# TASK: Console-Based Simple Calculator
#
# Build a calculator program that runs in the console and performs basic
# arithmetic operations based on the user's input.
#
# -----------------------------------------------------------------------------
# OPERATIONS YOUR CALCULATOR MUST SUPPORT
# -----------------------------------------------------------------------------
#
#   1. Addition          ( + )    e.g.  10 + 3  =  13
#   2. Subtraction       ( - )    e.g.  10 - 3  =  7
#   3. Multiplication    ( * )    e.g.  10 * 3  =  30
#   4. Division          ( / )    e.g.  10 / 3  =  3.33
#   5. Modulus           ( % )    e.g.  10 % 3  =  1  (remainder)
#   6. Exponentiation    ( ** )   e.g.  2 ** 8  =  256
#   7. Quit
#
# -----------------------------------------------------------------------------
# HOW THE MENU SHOULD LOOK
# -----------------------------------------------------------------------------
#
#   ============================
#        SIMPLE CALCULATOR
#   ============================
#   1. Addition
#   2. Subtraction
#   3. Multiplication
#   4. Division
#   5. Modulus
#   6. Exponentiation
#   7. Quit
#   Select an operation (1-7):
#
# -----------------------------------------------------------------------------
# EXPECTED INTERACTION EXAMPLE
# -----------------------------------------------------------------------------
#
#   Select an operation (1-7): 4
#   Enter first number : 10
#   Enter second number: 3
#   Result: 10 / 3 = 3.33
#
#   Select an operation (1-7): 4
#   Enter first number : 5
#   Enter second number: 0
#   Error: Cannot divide by zero.
#
#   Select an operation (1-7): 7
#   Goodbye!
#
# -----------------------------------------------------------------------------
# REQUIREMENTS
# -----------------------------------------------------------------------------
# - Each arithmetic operation MUST be written as its own function.
# - Use a loop so the calculator keeps running until the user selects Quit.
# - Division by zero must be caught and handled with a clear error message
#   (do NOT let the program crash).
# - Division results should be rounded to 2 decimal places.
# - Handle invalid menu choices gracefully.
#

#
# =============================================================================
# YOUR CODE BELOW — remove the # symbols from the scaffold and fill it in
# =============================================================================

 #Topic Multiple Arithmetic Operations

#Task : Console-Based Simple Calculator

def show_menu():
    print("\n============================")
    print("     SIMPLE CALCULATOR")
    print("============================")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Modulus")
    print("6. Exponentiation")
    print("7. Quit")

def calculate(choice, num1, num2):
    if choice == 1:
        result = num1 + num2
        print(f"Result: {num1} + {num2} = {result}")
    elif choice == 2:
        result = num1 - num2
        print(f"Result: {num1} - {num2} = {result}")
    elif choice == 3:
        result = num1 * num2
        print(f"Result: {num1} * {num2} = {result}")
    elif choice == 4:
        if num2 == 0:
            print("Error: Cannot divide by zero.")
        else:
            result = round(num1 / num2, 2)
            print(f"Result: {num1} / {num2} = {result}")
    elif choice == 5:
        if num2 == 0:
            print("Error: Cannot perform modulus by zero.")
        else:
            result = num1 % num2
            print(f"Result: {num1} % {num2} = {result}")
    elif choice == 6:
        result = num1 ** num2
        print(f"Result: {num1} ** {num2} = {result}")
    else:
        print("Invalid choice. Please select a number between 1 and 7.")

def calculator_app():
    while True:
        show_menu()
        choice = int(input("Select an operation (1-7): "))
        if choice == 7:
            print("Goodbye!")
            break
        num1 = float(input("Enter first number : "))
        num2 = float(input("Enter second number: "))
        calculate(choice, num1, num2)

if __name__ == "__main__":
    calculator_app()