import os
import re
from calculator import Calculator

clear = lambda: os.system('cls')
calculator = Calculator()



while True:

    clear()
    print("\nMenu of calculator\n"
          "range of numbers:[0...9]\n"
          "1 - add\n"
          "2 - subtract\n"
          "3 - multiply\n"
          "4 - divide\n"
          "5 - evaluate: [+, -, *, /, (, )]\n"
          "6 - exit\n")
    option = input("Choose command:")

    if option == '1':
        x = int(input("enter number X: "))
        y = int(input("enter number Y: "))
        try:
            print("Result of 'add': ", calculator.add(x, y))
        except NotImplementedError:
            print("It is not implemented, as the number is out of range")

    elif option == '2':
        x = int(input("enter number X: "))
        y = int(input("enter number Y: "))
        try:
            print("Result of 'subtract': ", calculator.subtract(x, y))
        except NotImplementedError:
            print("It is not implemented, as the number is out of range")

    elif option == '3':
        x = int(input("enter number X: "))
        y = int(input("enter number Y: "))
        try:
            print("Result of 'multiply': ", calculator.multiply(x, y))
        except NotImplementedError:
            print("It is not implemented, as the number is out of range")

    elif option == '4':
        x = int(input("enter number X: "))
        y = int(input("enter number Y: "))
        try:
            print("Result of 'divide': ", calculator.divide(x, y))
        except ZeroDivisionError:
            print("Is not divisible by zero")
        except NotImplementedError:
            print("It is not implemented, as the number is out of range")

    elif option == '5':
        x = input("enter evaluate, for example '2/3*4-(6+3)': ")
        control = re.compile('[^\(\)\d\*\+/-]+')
        if control.search(x) is None:
            try:
                print("Result of 'evaluate': ", calculator.evaluate(x))
            except SyntaxError:
                print("Syntax error, such as a missing parenthesis '(' or ')'")
            except ZeroDivisionError:
                print("Is not divisible by zero")
        else: print("Such an operation is not supported.\nSupported operations: +, -, *, /, (, )")

    elif option == '6':
        break

    else: print("Oops! Unknown option # %s" % option)










