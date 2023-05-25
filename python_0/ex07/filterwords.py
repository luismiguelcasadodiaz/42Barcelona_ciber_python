#!/usr/bin/python3
"""
Make a program that takes a string S and an integer N as
argument and print the list of words in S that contains
more than N non-punctuation characters.

• Words are separated from each other by space characters
• Punctuation symbols must be removed from the printed list:
    they are neither part of a word nor a separator
• The program must contains at least one list comprehension expression.


If the number of argument is different from 2,
or if the type of any argument is wrong,
the program prints an error message.
"""

import sys
import string


def remove_punctuation(the_list):
    """ For each word in the list, replace
    punctuaction car by empty char
    """
    my_list = the_list.copy()
    for idx, elem in enumerate(my_list):
        new_elem = ""
        for car in elem:
            if car not in string.punctuation:
                new_elem = new_elem + car
        my_list[idx] = new_elem
    return my_list


def fil_list(words, leng):
    words_list = words.split()
    words_list = remove_punctuation(words_list)
    result = [word for word in words_list if len(word) > leng]
    print(result)


if __name__ == "__main__":
    num_args = len(sys.argv)
    if num_args != 3:
        print("ERROR")
    elif sys.argv[2].isnumeric():
        fil_list(sys.argv[1], int(sys.argv[2]))
    else:
        print("ERROR")
