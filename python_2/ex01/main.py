#!/usr/local/bin/python3
"""
Instructions
In this exercise you have to implement a function named
what_are_the_vars which
returns an instance of class ObjectC.

ObjectC attributes are set via the parameters received
during the instanciation.

You will have to modify the ’instance’ ObjectC, NOT the class.

You should take a look to getattr, setattr built-in functions
"""


def what_are_the_vars(*args, **kwargs):
    """
      *args = a tuple of parameters
      **kwarg a dictionary of parameters
      '*' and '**' are unpacking operators
      '*' can be applied to any iterable but Dict
      '**' Can be applied to Dict
    returns an instance of class ObjectC.
    """
    try:
        # case WITHOUT key-word arguments
        if isinstance(args, tuple) and kwargs == {}:
            """
            print("wav_args    :", *args)
            for k,v in kwargs.items():
                print(f"wav_**kwargs:{k}-{v}")
            """
            return ObjectC(*args)

        # case WITH key-word arguments
        if isinstance(args, tuple) and kwargs != {}:
            """
            print("wav_args    :", *args)
            for k,v in kwargs.items():
                print(f"wav_**kwargs:{k}-{v}")
            """
            return ObjectC(*args, **kwargs)
    except AttributeError:
        return None


class ObjectC(object):
    def __init__(self, *args, **kwargs):
        # first: positional argumments
        # will follow the pattern var_0, var_1 ... var_n
        counter = 0
        var_name = "var_" + str(counter)
        if args != ():
            # print("obj_args    :", *args)
            for arg in args:
                self.__setattr__(var_name, arg)
                counter = counter + 1
                var_name = "var_" + str(counter)

        # second: kwy- word arguments
        if kwargs is not None and kwargs != {}:
            # detect if any key-word argument already exist
            # If one argument  is repeated raise exception
            for k, v in kwargs.items():
                if k in self.__dict__:
                    raise AttributeError
                else:
                    self.__dict__.update({k: v})

            """
            for k,v in kwargs.items():
                print(f"obj_**kwargs:{k}-{v}")
            """


def doom_printer(obj):
    if obj is None:
        print("ERROR")
        print("-----end-----")
        return
    for attr in dir(obj):
        if attr[0] != '_':
            value = getattr(obj, attr)
            print("\t{}: {}".format(attr, value))
    print("-----end-----")


if __name__ == "__main__":

    print("test==> what_are_the_vars(7)")
    print("Resu==> var_0: 7")
    obj = what_are_the_vars(7)
    doom_printer(obj)

    print("test==> what_are_the_vars(None, [])")
    print("Resu==> var_0: None | var_1: []")
    obj = what_are_the_vars(None, [])
    doom_printer(obj)

    print("test==> what_are_the_vars('ft_lol', 'Hi')")
    print("Resu==> var_0: ft_lol | var_1: Hi")
    obj = what_are_the_vars("ft_lol", "Hi")
    doom_printer(obj)

    print("test==> what_are_the_vars()")
    print("Resu==>")
    obj = what_are_the_vars()
    doom_printer(obj)

    print("test==> what_are_the_vars(12, 'Yes', [0, 0, 0], a=10, hello='world')")
    print("Resu==> a: 10 | hello: world |var_0: 12 | var_1: Yes | var_2: [0, 0, 0]")
    obj = what_are_the_vars(12, "Yes", [0, 0, 0], a=10, hello="world")
    doom_printer(obj)

    print("test==> what_are_the_vars(42, a=10, var_0='world')")
    print("Resu==> ERROR")
    obj = what_are_the_vars(42, a=10, var_0="world")
    doom_printer(obj)

    print("test==> what_are_the_vars(42, 'Yes', a=10, var_2='world')")
    print("Resu==> a: 10 | var_0: 12 | var_1: Yes | var_2: world")
    obj = what_are_the_vars(42, "Yes", a=10, var_2="world")
    doom_printer(obj)
