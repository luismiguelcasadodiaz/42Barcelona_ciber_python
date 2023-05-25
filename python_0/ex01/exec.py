#!/usr/bin/python3
""" Make a program that takes a string as argument,
    reverses it, swaps its letters case
    and print the result.
    • If more than one argument are provided,
      merge them into a single string with each
      argument separated by a space character.
    • If no argument are provided, do nothing or print an usage.
"""


import sys
import string

def reverse_str(text: str) -> str:

    """
    PARAMETERS
        Text to reverse
    RETURNS
        Reversed text

    This function reverse the string using [-1::-1] notation
    that is :start in the last char and step towarda the left
    one char aeach time
    """
    return text[-1::-1]


def swap_case(text: str) -> str:

    """
    PARAMETERS
        Text to swap cases
    RETURNS
        Text wiht swapped case
    """
    swapped_text = ""
    for y in range(len(text)):
        if text[y] in string.punctuation:
            swapped_text = swapped_text + text[y]
        elif text[y].isupper():
            swapped_text = swapped_text + text[y].lower()
        else:
            swapped_text = swapped_text + text[y].upper()
    return swapped_text


def treat_argv(arguments: list) -> str:

    """
    PARAMETERS
        arguments: a list with arguments passed to this script
    RETURNS
        a string that joins all arguments separated by space
    """
    return " ".join(arguments)


if __name__ == "__main__":
    if len(sys.argv) == 1:
        print("Usage is: exec.py string1 string2 stringN")
        sys.exit(-1)
    else:
        print(sys.argv[1:])
        text_to_reverse = treat_argv(sys.argv[1:])
        reversed_text = reverse_str(text_to_reverse)
        swapped = swap_case(reversed_text)
        print(swapped)
