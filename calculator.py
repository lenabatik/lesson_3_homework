
class Calculator:
    def __init__(self):
        self.base_numeral_system = 10

    def add(self, x, y):
        """This function adds two numbers"""
        if self.range_checking(x):
            if self.range_checking(y):
                return x + y
        raise NotImplementedError

    def subtract(self, x, y):
        """This function subtracts two numbers"""
        if self.range_checking(x):
            if self.range_checking(y):
                return x - y
        raise NotImplementedError

    def multiply(self, x, y):
        """This function multiplies two numbers"""
        if self.range_checking(x):
            if self.range_checking(y):
                return x * y
        raise NotImplementedError

    def divide(self, x, y):
        """This function divides two numbers"""
        if self.range_checking(x):
            if self.range_checking(y):
                if y == 0:
                    raise ZeroDivisionError
                else: return x / y
        raise NotImplementedError

    def evaluate(self, expression):
        """This function evaluate expression"""
        return eval(expression)

    def range_checking(self, variable):
        if variable >= 0 and variable < self.base_numeral_system:
            return 1
        return 0


