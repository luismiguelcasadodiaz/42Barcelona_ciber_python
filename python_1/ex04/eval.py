#!/usr/bin/python3
"""
Objective:

The goal of the exercise is to discover 2 useful methods for lists, tuples,
dictionnaries (iterable class objects more generally) named zip and enumerate.

Instructions
Code a class Evaluator, that has two static functions named zip_evaluate
and enumerate_evaluate.

The goal of these 2 functions is to compute the sum of:
  -- the words of every words of a given list
  -- weighted by a list of coefficinents coefs

  (yes, the 2 functions should do the same thing).


The lists coefs and words have to be the same length.
If this is not the case, the function should return -1.


You have to obtain the desired result using zip in the zip_evaluate function,
and with enumerate in the enumerate_evaluate function
"""


class Evaluator:
    def __init__(self):
        pass

    @staticmethod
    def zip_evaluate(coefs: list, words: list) -> int:
        """ multiplies the word's lenght times coef
        PARAM
                words: a list of words
                coefs: a list oof coeficients
        RETURN
                the sum the results form multiply words's lengt by coefs
        """

        # When both list has equal length we can zip them
        # resulting a new list of tuples with one member
        # from each zipped list (word1, coef1), (word2, coef2)

        if len(words) == len(coefs):
            zipped = zip(words, coefs)
            # the list comprenhension convers a list of tuples [(w,c)..(w,c)]
            # into a list on numbers, whose sum i return
            return sum([len(word) * coef for word, coef in zipped])
        else:
            return -1

    @staticmethod
    def enumerate_evaluate(coefs: list, words: list) -> int:
        """ multiplies the word's lenght times coef
        PARAM
                words: a list of words
                coefs: a list oof coeficients
        RETURN
                the sum the results form multiply words's lengt by coefs
        """

        # When both list has equal it is possible to loop over
        # them simultaneously.
        # We use the index of word inside the words list
        # to access the relevant coef in the coefs list

        if len(words) == len(coefs):
            return sum([len(word) * coefs[index]
                        for index, word in enumerate(words)])
        else:
            return -1


if __name__ == "__main__":
    words = ["Le", "Lorem", "Ipsum", "est", "simple"]
    coefs = [1.0, 2.0, 1.0, 4.0, 0.5]
    result1 = Evaluator.zip_evaluate(coefs, words)
    result2 = Evaluator.enumerate_evaluate(coefs, words)

    words = ["Le", "Lorem", "Ipsum", "n’", "est", "pas", "simple"]
    coefs = [0.0, -1.0, 1.0, -12.0, 0.0, 42.42]
    result3 = Evaluator.enumerate_evaluate(coefs, words)

    print(f"Resultado del test 1 es {result1}")
    print(f"Resultado del test 2 es {result2}")
    print(f"Resultado del test 3 es {result3}")
