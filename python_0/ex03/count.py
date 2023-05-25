#!/usr/bin/python3
""" Create a function called text_analyzer
    that takes a single string argument and displays
    the sums of its
    upper-case characters,
    lower-case characters,
    punctuation characters and
    spaces.
    • If None or nothing is provided
        the user is prompted to provide a string.
    • If the argument is not a string
        print an error message.
    • This function must have a docstring explaning its behavior.
"""


import string
import sys


def format_output(tot: int, up: int, lo: int, pu: int, sp: int):
    print("The text contains {} character(s):".format(tot))
    print("- {} upper letter(s)".format(up))
    print("- {} lower letter(s)".format(lo))
    print("- {} punctuation mark(s)".format(pu))
    print("- {} space(s)".format(sp))


def counter(arg: str):
    # counters set up
    tot = len(arg)
    up = 0
    lo = 0
    pu = 0
    sp = 0
    for i in range(tot):
        if arg[i].isupper():
            up = up + 1
        elif arg[i].islower():
            lo = lo + 1
        elif arg[i] in string.punctuation:
            pu = pu + 1
        elif arg[i].isspace():
            sp = sp + 1

    format_output(tot, up, lo, pu, sp)


def ask_txt() -> str:
    correct_arg = False
    while not correct_arg:                     # so i read one
        the_arg = input("Please enter the text to analyse:").strip()
        if len(the_arg) != 0:
            try:
                the_arg = int(the_arg)         # and check is not int
                print("AssertionError: argument is not a string")
            except ValueError:
                correct_arg = True
    return the_arg


def text_analyser(*my_arg):
    """
    This function counts the number of upper characters,
    lower characters, punctuation and spaces in a given text.
    PARAMETERS
        a text string to make statisics on it
    RETURNS
        nothing
    """
    print(my_arg, len(my_arg))
    if len(my_arg) > 1:  # more than one argument
        print("This function only accepts one argument")
        return
    if my_arg == () or my_arg == ('',):            # i got no argument
        the_arg = ask_txt()
    else:                                          # I got  one argument
        try:
            print(my_arg[0])
            the_arg = int(my_arg[0])         # and check if int
            print("AssertionError: argument is not a string")
            the_arg = ask_txt()              # as it is i ask new argument
        except ValueError:
            the_arg = my_arg[0]              # as it is not i procced
    counter(the_arg)


if __name__ == "__main__":
    num_args = len(sys.argv)
    if num_args == 1:
        text_analyser("")
    elif num_args == 2:
        text_analyser(sys.argv[1])
    else:
        print("Usage is: count.py <string>")
        sys.exit(-1)
