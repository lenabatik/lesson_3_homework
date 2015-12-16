import os
import re
from calculator import Calculator

clear = lambda: os.system('cls')
calculator = Calculator()

def options_of_menu(option):
    if option in {'1', '2', '3', '4'}:
        x = int(input("enter number X: "))
        y = int(input("enter number Y: "))
        if option == '1':
            print("Result of 'add': ", calculator.add(x, y))
        elif option == '2':
            print("Result of 'subtract': ", calculator.subtract(x, y))
        elif option == '3':
            print("Result of 'multiply': ", calculator.multiply(x, y))
        elif option == '4':
            print("Result of 'divide': ", calculator.divide(x, y))
    elif option == '5':
        x = input("enter evaluate, for example '2/3*4-(6+3)': ")
        control = re.compile('[^\(\)\d\*\+/-]+')
        if control.search(x) is None:
            print("Result of 'evaluate': ", calculator.evaluate(x))
        else: print("Such an operation is not supported.\nSupported operations: +, -, *, /, (, )")
    elif option == '6':
        return 1
    else: print("Oops! Unknown option # %s" % option)
    return 0

flag = 0

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
    
    try:
        flag = options_of_menu(option)
    except ValueError:
        print("Incorrect number format. Range of numbers:[0...9]")
    except ZeroDivisionError:
        print("Is not divisible by zero")
    except SyntaxError:
        print("Syntax error, such as a missing parenthesis '(' or ')'")

    if flag:
        break
