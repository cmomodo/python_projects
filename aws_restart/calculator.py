from operator import sub, add, mul, truediv


def calculator():
    print("""
    + - Addition
    - - Subtraction
    * - Multiplication
    / - Division
    """)
    print("Please enter the first number:")
    num1 = int(input(':'))
    print("Please enter the second number:")
    num2 = int(input(':'))
    print("Please enter the operator:")
    operators = {'+': add, '-': sub, '*': mul, '/': truediv}
    operator = input(':')
    print(operators.get(operator, invalid)(num1, num2))



def invalid():
    return "Invalid operator"


calculator()