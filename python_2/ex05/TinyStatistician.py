#!/usr/local/bin/python3
"""
Objective

Initiation to very basic statistic notions.

Instructions
Create a class named TinyStatistician that implements the following methods:

• mean(x): computes the mean of a given non-empty list or array x, using a
for-loop.
The method returns the mean as a float, otherwise None if x is an empty list
or array. Given a vector x of dimension m × 1, the mathematical formula of
its mean:

• median(x): computes the median of a given non-empty list or array x. The
method returns the median as a float, otherwise None if x is an empty list or
array.

• quartiles(x): computes the 1st and 3rd quartiles of a given non-empty array
x. The method returns the quartile as a float, otherwise None if x is an empty
list or array.


• var(x): computes the variance of a given non-empty list or array x, using a
forloop. The method returns the variance as a float, otherwise None if x is an
empty list or array. Given a vector x of dimension m × 1, the mathematical
formula of its variance is:

• std(x) : computes the standard deviation of a given non-empty list or array
x, using a for-loop. The method returns the standard deviation as a float,
otherwise None if x is an empty list or array. Given a vector x of dimension
m × 1, the mathematical formula of its standard deviation is:

All methods take a list or a numpy.ndarray as parameter.
We are assuming that all inputs have a correct format, i.e. a list or array of
numeric type or empty list or array. You don’t have to protect your functions
against input errors.

"""
from numpy import ndarray


class TinyStatistician():

    def valid(self, data):
        """
            Validate if data is list or ndarray
            As ndarray already has all elements of same type i check that
            the list has all elements of same type.

            RETURNS:
            a tuple (bool, list)
            the bool part of the tuple to say if data ara valida or not
                    (True, list of data)
                    (False, None)

        """
        try:
            if isinstance(data, (list, ndarray)):
                if isinstance(data, ndarray):
                    data = data.tolist()

                check = map(lambda x: isinstance(x, (int, float)), data)
                if all(check):
                    return True, data.sort()
                else:
                    msg = "Data does not have all elements of same type"
                    raise ValueError(msg)
            else:
                # we will treat only lists od arrays
                raise ValueError("Not list or array")
        except ValueError as msg:
            print("TinyStatistician:", msg)
            return False, None

    def mean(self, data):
        data_ok, my_data = self.valid(data)
        if data_ok:
            result = sum(data) / len(data)
            return float(result)
        else:
            return None

    def median(self, data):
        data_ok, my_data = self.valid(data)
        if data_ok:
            size = len(data)
            if size % 2 == 0:
                n1 = data[(size // 2) - 1]
                n2 = data[(size // 2)]
                result = (n1 + n2)/2
            else:
                # odd numbers. Remembera that losts are Zero base indez
                result = data[(size // 2)]
            return float(result)
        else:
            return None

    def my_quartil(self, idx, data):

        if idx == idx // 1:
            # integer index
            return data[int(idx) - 1]
        else:
            # float index
            basenum = data[int(idx // 1) - 1]
            nextbasenum = data[int(idx // 1)]
            diff = nextbasenum - basenum
            coef = idx - (idx // 1)
            basenum = basenum + diff * coef
            return basenum

    def quartiles(self, data):
        data_ok, my_data = self.valid(data)
        if data_ok:
            iq1 = (len(data) + 1) / 4
            q1 = self.my_quartil(iq1, data)
            q3 = self.my_quartil(3 * iq1, data)
            return [q1, q3]
        else:
            return None

    def var(self, data):
        data_ok, my_data = self.valid(data)
        if data_ok:
            m = len(data)
            mu = self.mean(data)
            numerator = sum(map(lambda x: (x - mu) ** 2, data))
            return numerator / m
        else:
            return None

    def std(self, data):
        data_ok, my_data = self.valid(data)
        if data_ok:
            return self.var(data) ** (1/2)
        else:
            return None
