#!/usr/bin/python3


def has_only_one_parameter(fun) -> bool:
    """
    https: //stackoverflow.com/questions/847936/
    how-can-i-find-the-number-of-arguments-of-a-python-function
    """
    return (fun.__code__.co_argcount == 1)


def ft_map(fun,  ite):
    """Map the function to all elements of the iterable.
    Args:
    function_to_apply:  a function taking an iterable.
    iterable:  an iterable object (list,  tuple,  iterator).
    Return:
    An iterable.
    None if the iterable can not be used by the function.
    """
    try:
        if ite is not None and fun is not None:

            if not has_only_one_parameter(fun):
                msg = f"function '{fun.__name__}' accepts\
                      more than one parameter"
                raise ValueError(msg)
            else:
                msg = ""
                result = []
                for elem in ite:
                    result.append(fun(elem))

                if isinstance(ite,  list):
                    yield result
                if isinstance(ite,  tuple):
                    yield tuple(result)
                if isinstance(ite,  dict):
                    yield dict(zip(ite.keys(),  result))
                if isinstance(ite,  set):
                    yield set(result)
                if isinstance(ite,  str):
                    yield ''.join(result)
        else:
            if fun is not None:
                msg = f"Can not filter object {ite} \
                    with function {fun.__name__}"
            else:
                msg = f"Can not filter object {ite} \
                    with function {fun}"
            raise ValueError("ft_filter:  " + msg)
    except Exception as e:
        print(e)
