#!/usr/bin/python3
""" Make a program that takes a number as argument,
    checks whether it is odd, even or
    zero, and print the result.
    • If more than one argument are provided or if the argument isi
    not an integer, print an error message.
    • If no argument are provided, do nothing or print an usage.
"""

import sys


def treat_argv(argument: int) -> str:

    """
    PARAMETERS
        argument: An integer to  analise
    RETURNS
        a string describing the integer

    """
    descriptions = ["I'm Zero", "I'm Odd", "I'm Even"]
    if argument == 0:
        index = 0
    elif argument % 2 == 0:
        index = 2
    else:
        index = 1
    return descriptions[index]


if __name__ == "__main__":
    num_args = len(sys.argv)
    if num_args == 1:
        print("Usage is: whois.py Number")
        sys.exit(-1)
    elif num_args > 2:
        print("AssertionError: more than one argument are provided")
    else:
        try:
            number_to_evaluate = int(sys.argv[1])
        except ValueError:
            print("AssertionError: argument is not an integer")
            sys.exit(-1)
        else:
            result = treat_argv(number_to_evaluate)
            sys.exit(result)
