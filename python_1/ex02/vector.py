#!/usr/bin/python3

class Vector:
    def __init__(self, argument):
        self.values = argument
        self.shape
        self.__type

    @property
    def values(self) -> list:
        return self._values

    @values.setter
    def values(self, argument):
        # initialize as a list
        if isinstance(argument, list):
            # check is first list's element is a list
            if isinstance(argument[0], list):
                self.treat_list_of_lists(argument)
            else:
                raise ValueError(f"{argument} is not a list of list")

        # initialize as size
        elif isinstance(argument, int):
            if argument == 0:
                msg = f"imposible init vector wiht {argument} elemens"
                raise ValueError(msg)
            else:
                values_list = []
                for i in range(argument):
                    values_list.append([float(i)])
                self._values = values_list
                self.shape = (len(self.values), 1)
                self.__type = "COL"

        # initialize as a range
        elif isinstance(argument, tuple):
            # TODO: text if > or >=
            if argument[0] > argument[1]:
                raise ValueError(f"imposible init vector with {argument}")
            else:
                try:
                    values_list = []
                    for i in range(argument[0], argument[1]):
                        values_list.append([float(i)])
                    self._values = values_list
                    self.shape = (len(self.values), 1)
                    self.__type = "COL"
                except Exception:
                    raise ValueError(f"Imposible init vector with {argument}")

    def treat_list_of_lists(self, argument):
        # it is a list of A list of floats
        # [[1.0, 2.0, 3.0, 4.0]]
        # i check >= cause
        # [[a]] is a valid row vector
        # [[a]] is a valid column vector
        values_list = []
        if len(argument) == 1 and len(argument[0]) >= 1:
            for num in argument[0]:
                if isinstance(num, str):
                    # [ 1.0, "a", 2.0]
                    # a non numeric list member
                    msg = f"imposible create a ROW vector with string {num}"
                    raise ValueError(msg)
                else:
                    values_list.append(float(num))
            self._values = [values_list]
            self.shape = (1, len(self.values[0]))
            self.__type = "ROW"
        elif len(argument) >= 1:
            # it is a list of LISTS of single float
            # [[1.0],[2.0],[3.0],[4.0]]
            for num in argument:
                if isinstance(num, list):
                    if len(num) == 1:
                        if isinstance(num[0], str):
                            # [[1.0],["2.0"],[3.0],[4.0]]
                            # one list member contains string
                            msg = f"imposible create COL vector with {num}"
                            raise ValueError(msg)
                        else:
                            values_list.append(num)
                    else:
                        # [[1.0],[2.0, 2.1],[3.0],[4.0]]
                        # a list member with more than one element
                        msg = f"imposible create COL vector with {num}"
                        raise ValueError(msg)
                else:
                    # [[ 1,0] , 2.0, [3.0]]
                    # one list member is not a list
                    raise ValueError(f"imposible create COL vector with {num}")
            self._values = values_list
            self.shape = (len(values_list), 1)
            self.__type = "COL"

    def T(self):
        """
        Transposes a vectors:
        ROW CASE
        [[0.0, ... , n.0]]  ==> [[0.0], ..., [n.0]]
        (1, n) ==> (n, 1)
        COL CASE
        [[0.0], ..., [n.0]] ==> [[0.0, ... , n.0]]
        (n, 1) ==> (1, n)
        """
        thevalues = self.values.copy()
        values_list = []
        if self.__type == "ROW":
            # i am a ROW
            for num in thevalues[0]:
                values_list.append([num])
            # transposed to a COL
            self._values = values_list
            self.shape = (len(values_list), 1)
            self.__type = "COL"

        else:
            # I am a COL
            for num in thevalues:
                values_list.append(num[0])
            # transpoosed to a ROW
            self._values = [values_list]
            self.shape = (1, len(values_list))
            self.__type = "ROW"

    def dot(self, obj):
        """
        Dot product vetween two vector of same dimension
        """
        if self.shape == obj.shape:
            sum = 0
            if self.shape[0] == 1:
                # both ROW vectors
                # [[0.0, ... , n.0]] . [[0.0, ... , n.0]]
                for idx in range(self.shape[1]):
                    sum = sum + self.values[0][idx] * obj.values[0][idx]
            if self.shape[1] == 1:
                # both COL vectors
                # [[0.0], ..., [n.0]] . [[0.0], ..., [n.0]]
                for idx in range(self.shape[0]):
                    sum = sum + self.values[idx][0] * obj.values[idx][0]
            return sum
        else:
            raise ValueError(f"impossible dot product between {self.shape} \
                             and {obj.shape}")

    # __str__ & __repr__ must be identical, i.e we expect that print(vector)
    # and vector within python interpretor behave the same, see correspondi
    def __str__(self):
        return f"{self.__class__.__name__}({self.values})"

    def __repr__(self):
        return f"{self.__class__.__name__}({self.values})"

    # add & radd : only vectors of same shape.

    def __add__(self, other):
        """
        Adds two vectors with same shape :vector + vector
        x = [[0.0, 1.0, 2.0, 3.0]] + Vector(4)
        here self holds  [[0.0, 1.0, 2.0, 3.0]] and other holds Vector(4)

        """
        if isinstance(other, Vector):
            if self.shape == other.shape:
                result_list = []
                if self.shape[0] == 1:
                    # both ROW vectors
                    # [[0.0, ... , n.0]] . [[0.0, ... , n.0]]
                    for idx in range(self.shape[1]):
                        result_list.append(self.values[0][idx] +
                                           other.values[0][idx])
                    return Vector([result_list])
                if self.shape[1] == 1:
                    # both COL vectors
                    # [[0.0], ..., [n.0]] . [[0.0], ..., [n.0]]
                    for idx in range(self.shape[0]):
                        result_list.append([self.values[idx][0] +
                                            other.values[idx][0]])
                    return Vector(result_list)
            else:
                msg = f"ADD:Shape {self.shape} is\
                      not compatible with {other.shape}"
                raise ValueError(msg)
        else:
            raise ValueError(f"ADD:'{other}' is not a vector")

    def __radd__(self, other):
        return self.__add__(other, self)

    # sub & rsub: only vectors of same shape.

    def __sub__(self, other):
        """
        Substract two vectors with same shape :vector - vector
        x = [[0.0, 1.0, 2.0, 3.0]] - Vector(4)
        here self holds  [[0.0, 1.0, 2.0, 3.0]] and other holds Vector(4)

        """
        if isinstance(other, Vector):
            if self.shape == other.shape:
                result_list = []
                if self.shape[0] == 1:
                    # both ROW vectors
                    # [[0.0, ... , n.0]] . [[0.0, ... , n.0]]
                    for idx in range(self.shape[1]):
                        result_list.append(self.values[0][idx] -
                                           other.values[0][idx])
                    return Vector([result_list])
                if self.shape[1] == 1:
                    # both COL vectors
                    # [[0.0], ..., [n.0]] . [[0.0], ..., [n.0]]
                    for idx in range(self.shape[0]):
                        result_list.append([self.values[idx][0] -
                                            other.values[idx][0]])
                    return Vector(result_list)
            else:
                msg = f"SUB:Shape {self.shape} is\
                     compatible with {other.shape}"
                raise ValueError(msg)
        else:
            raise ValueError(f"SUB:'{other}' is not a vector")

    def __rsub__(other, self):
        return self.__sub__(other, self)

    # truediv : only with scalars (to perform division of Vector by a scalar).
    def __truediv__(self, other):
        """
        divide a vector / Scalar
        x = Vector(4) / 5
        here self holds the vector and other holds 5
        """
        if isinstance(other, int) or isinstance(other, float):
            if other == 0:
                raise ValueError(f"TRUEDIV: {other} is not a good divisor")
            result_list = []
            if self.shape[0] == 1:
                # both ROW vectors
                # [[0.0, ... , n.0]] . [[0.0, ... , n.0]]
                for idx in range(self.shape[1]):
                    result_list.append(self.values[0][idx] / other)
                return Vector([result_list])
            if self.shape[1] == 1:
                # both COL vectors
                # [[0.0], ..., [n.0]] . [[0.0], ..., [n.0]]
                for idx in range(self.shape[0]):
                    result_list.append([self.values[idx][0] / other])
                return Vector(result_list)
        else:
            msg = f"TRUEDIV: '{other}' \
                   is not an escalar to divide by"
            raise ValueError(msg)

    # rtruediv : raises NotImplementedError with the message
    # "Division of a scalar by a Vector is not defined here."

    def __rtruediv__(other, self):
        """
        divide an scalar * vector
        x = 5 / Vector(4)
        here self holds 5 and other holds the vector
        """
        if self is None:
            msg = f"RTRUEDIV:Division of a {self} \
                    by a Vector is not possible"
            raise ValueError(msg)
        else:
            msg = f"RTRUEDIV:Division of a scalar {other} \
                by a Vector is not defined here."
            raise NotImplementedError(msg)

    # mul & rmul: only SCALARS (multiplies Vectors and scalars).

    def __mul__(self, other):
        """
        multiplies a vector * Scalar
        x = Vector(4) * 5
        here self holds the vector and other holds 5

        """
        if isinstance(other, int) or isinstance(other, float):
            result_list = []
            if self.shape[0] == 1:
                # both ROW vectors
                # [[0.0, ... , n.0]] . [[0.0, ... , n.0]]
                for idx in range(self.shape[1]):
                    result_list.append(self.values[0][idx] * other)
                return Vector([result_list])
            if self.shape[1] == 1:
                # both COL vectors
                # [[0.0], ..., [n.0]] . [[0.0], ..., [n.0]]
                for idx in range(self.shape[0]):
                    result_list.append([self.values[idx][0] * other])
                return Vector(result_list)
        else:
            raise ValueError(f"MUL:'{other}' not escalar to multiply by")

    def __rmul__(other, self):
        """
        multiplies an scalar * vector
        x = 5 * Vector(4)
        here self holds 5 and other holds the vector

        """
        if isinstance(self, int) or isinstance(self, float):
            result_list = []
            if other.shape[0] == 1:
                # both ROW vectors
                # [[0.0, ... , n.0]] . [[0.0, ... , n.0]]
                for idx in range(other.shape[1]):
                    result_list.append(other.values[0][idx] * self)
                return Vector([result_list])
            if other.shape[1] == 1:
                # both COL vectors
                # [[0.0], ..., [n.0]] . [[0.0], ..., [n.0]]
                for idx in range(other.shape[0]):
                    result_list.append([other.values[idx][0] * self])
                return Vector(result_list)
        else:
            raise ValueError(f"RMUL:'{self}' not escalar to multiply by")
