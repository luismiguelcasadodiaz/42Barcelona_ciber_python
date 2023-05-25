#!/usr/bin/python3
import string
import sys
"""
Make a program that takes a string as argument and encode it into Morse code.
• The program supports space and alphanumeric characters
• An alphanumeric character is represented by dots . and dashes -:
• A space character is represented by a slash /
• Complete morse characters are separated by a single space

If more than one argument are provided, merge them into a single string
with each argument separated by a space character.
If no argument is provided, do nothing or print an usage
"""
table_morse = {
    'A': '.-',
    'B': '-...',
    'C': '-.-.',
    'D': '-..',
    'E': '.',
    'F': '..-.',
    'G': '--.',
    'H': '....',
    'I': '..',
    'J': '.---',
    'K': '-.-',
    'L': '.-..',
    'M': '--',
    'N': '-.',
    'O': '---',
    'P': '.--.',
    'Q': '--.-',
    'R': '.-.',
    'S': '...',
    'T': '-',
    'U': '..-',
    'V': '...-',
    'W': '.--',
    'X': '-..-',
    'Y': '-.--',
    'Z': '--..',
    '0': '-----',
    '1': '.----',
    '2': '..---',
    '3': '...--',
    '4': '....-',
    '5': '.....',
    '6': '-....',
    '7': '--...',
    '8': '---..',
    '9': '----.',
    ' ': '/'
}


def convert(txt):
    print(txt)
    # Verify that only spaces and alphanumerics
    for car in txt:
        if car in string.punctuation:
            print("ERROR")
            return
    capi_txt = txt.upper()
    for i in range(len(txt)):
        print(table_morse[capi_txt[i]], " ", end="")
    print()


if __name__ == "__main__":
    num_args = len(sys.argv)
    if num_args == 1:
        print("Usage is: sos.py <string1> <strind2> .. <stringN>")
    else:
        txt = " ".join(sys.argv[1:])
        convert(txt)
