#!/usr/bin/python3
"""
Objective
The goal of the exercise is to discover the concept of generator
object in Python.

Instructions
Code a function called generator that takes a text as input,
(only printable characters), uses the string parameter sep as a splitting
parameter, and yields the resulting substrings.

The function can take an optional argument. The options are:
• shuffle: shuffles the list of words,
• unique: returns a list where each word appears only once,
• ordered: alphabetically sorts the words.



"""
import string
import random


def all_are_printable(text: str) -> bool:
    """ Verifies that each char of text is printable"""
    all_are = True
    for char in text:
        if char not in string.printable:
            all_are = False
            break
    return all_are


def unique(onelist: list) -> list:
    """
    PARAMETER
            A list of words
    RETURNS
            A list with unique words in the list

    This function uses a set to group unique words

    """

    # converts the list into a set
    set_of_list = set(onelist)
    # converts the set into a list
    unique_list = list(set_of_list)
    return unique_list


def myshuffle(onelist: list) -> list:
    random.shuffle(onelist)
    return onelist


# function prototype
def generator(text, sep=" ", option=None):
    """
    Splits the text according to sep value and yield the substrings.
    option precise if a action is performed to the substrings before
    it is yielded.
    PARAM
            text : the text to split
            sep  : the character to explit on

    RETURN
    """
    result = ["ERROR"]
    if isinstance(text, str):
        if not all_are_printable(text):
            pass
            # result = ["ERROR"]
            # raise ValueError("The text contains non printable characters")
        else:
            splitted = text.split(sep)
            if option is None:
                result = splitted
            elif option == "shuffle":
                result = myshuffle(splitted)
            elif option == "unique":
                result = unique(splitted)
            elif option == "ordered":
                result = sorted(splitted)
            else:
                pass
                # result = ["ERROR"]
                # raise ValueError(f"Option {option} is not available")
    else:
        pass
        # result = ["ERROR"]
    for word in result:
        yield word


if __name__ == "__main__":

    text = "Le Lorem Ipsum est simplement du faux texte."
    print(f"{text} sep=' ' option none")
    for word in generator(text, sep=" "):
        print(word)
    print(f"{text} sep=' ' option shuffle")
    for word in generator(text, sep=" ", option="shuffle"):
        print(word)
    print(f"{text} sep=' ' option shuffle2")
    for word in generator(text, sep=" ", option="shuffle"):
        print(word)
    print(f"{text} sep=' ' option none")
    for word in generator(text, sep=" ", option="ordered"):
        print(word)

    text = "Lorem Ipsum Lorem Ipsum"
    for word in generator(text, sep=" ", option="unique"):
        print(word)
    text = 1.0
    for word in generator(text, sep="."):
        print(word)

    print("-" * 75)
    txt = "This is a simple string for a basic test. Very simple."
    for elem in generator(txt, sep=' '):
        print(elem)
    for elem in generator(txt, sep='.'):
        print(elem)
    for elem in generator(txt, sep='i'):
        print(elem)
    for elem in generator(txt, sep='si'):
        print(elem)
