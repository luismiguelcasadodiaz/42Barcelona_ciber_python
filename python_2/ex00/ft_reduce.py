#!/usr/bin/python3


def has_only_two_parameter(fun) -> bool:
    return (fun.__code__.co_argcount == 2)


def ft_reduce(fun, ite):
    """Apply function of two arguments cumulatively.
    Args:
        function_to_apply: a function taking an iterable.
        iterable: an iterable object (list, tuple, iterator).
    Return:
        A value, of same type of elements in the iterable parameter.
        None if the iterable can not be used by the function.
    """
    # ... Your code here ..
    try:
        if ite is not None and fun is not None:

            if not has_only_two_parameter(fun):
                msg = f"function '{fun.__name__}' has\
                      not two parameters"
                raise ValueError(msg)
            else:
                if isinstance(ite, (tuple | set | list)):
                    my_ite = list(ite)
                if isinstance(ite, dict):
                    my_ite = list(ite.values())

                msg = ""
                result = my_ite[0]
                for elem in my_ite[1:]:
                    result = fun(result, elem)

                if isinstance(ite,  list):
                    return result
                if isinstance(ite,  tuple):
                    return result
                if isinstance(ite,  dict):
                    return result
                if isinstance(ite,  set):
                    return result
                if isinstance(ite,  str):
                    return ''.join(result)
        else:
            if fun is not None:
                msg = f"Can not filter object {ite} \
                    with function '{fun.__name__}'"
            else:
                msg = f"Can not filter object {ite} \
                    with function {fun}"
            raise ValueError("ft_filter:  " + msg)
    except Exception as e:
        print(e)
