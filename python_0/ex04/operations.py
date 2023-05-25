#!/usr/bin/python3
"""
Write a program that takes two integers A and B as arguments and
prints the result of the following operations:

Sum:         A+B
Difference:  A-C
Product:     A*B
Quotient:    A/B
Remainder:   A%B

• If more or less than two argument are provided or
    if either of the argument is not an integer, print an error message.
• If no argument are provided, do nothing or print an usage.
• If an operation is impossible,
    print an error message instead of a numerical result.

"""
import LMCD_decorators
import sys

@LMCD_decorators.debug
def operate(a: int, b: int):
    print("Sum:         {}".format(a + b))
    print("Difference:  {}".format(a - b))
    print("Product:     {}".format(a * b))
    print("Quotient:    {}".format(
        a / b if b != 0 else "ERROR (division by zero)"))
    print("Remainder:   {}".format(
        a % b if b != 0 else "ERROR (modulo by zero)"))


if __name__ == "__main__":
    num_args = len(sys.argv)
    if num_args < 3:
        print("Usage is: python operations.py <number1> <number2>")
        print("Example:")
        print("\tpython operations 10 3")
        sys.exit(-1)
    elif num_args > 3:
        print("AssertionError: too many arguments")
        sys.exit(-1)
    else:
        try:
            a = int(sys.argv[1])
            b = int(sys.argv[2])
            operate(a, b)
        except:
            print("AssertionError: only integers")
