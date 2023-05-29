#!/usr/local/bin/python3
from ft_filter import ft_filter
from ft_map import ft_map
from ft_reduce import ft_reduce


if __name__ == '__main__':

    print("="*80)
    print("\t\t\t\t\tProbando ft_filter")
    print("="*80)

    my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    my_set_ = set(my_list)
    my_tupl = tuple(my_list)
    my_dict = {1: 1, 2: 2, 3: 3, 4: 4, 5: 5, 6: 6, 7: 7, 8: 8, 9: 9, 10: 10}
    my_stri = "1234b67890"

    def even(elem):
        return (elem % 2 == 0)

    def filter_b(elem):
        return (elem == 'b')
    print("======================testing Extrem cases ====================")
    print("==>ft_filter(None, None)")
    print(ft_filter(None, None))

    print("==>ft_filter(even, None)")
    print(ft_filter(even, None))

    print("==>ft_filter(None, my_list)")
    print(ft_filter(None, my_list))

    print("==>ft_filter(my_dict, my_list)")
    print(ft_filter(my_dict, my_list, ))
    print("======================testing list ==========================")
    print("==>ft_filter(filter_b, my_list)")
    print(ft_filter(filter_b, my_list))

    print("==>ft_filter(even, my_list)")

    for elem in ft_filter(even, my_list):
        print(elem)
    print("Original list ==>", my_list)

    print("==>ft_filter(even, [])")
    print(ft_filter(even, []))
    for elem in ft_filter(even, []):
        print(elem)
    print("======================testing sets ==========================")
    print("==>ft_filter(filter_b, ()))")
    print(ft_filter(filter_b, set()))

    print("==>ft_filter(even, my_set_)")
    print(ft_filter(even, my_set_))
    for elem in ft_filter(even, my_set_):
        print(elem)
    print("Original Set ==>", my_set_)   
    print("==>ft_filter(even,[])")
    print(ft_filter(even, set()))
    
    print("==>ft_filter(lambda x: x > 3, my_set_)")
    print(ft_filter(lambda x: x > 3, my_set_))
    for elem in ft_filter(lambda x: x > 3, my_set_):
        print(elem)
    print("Original Set ==>", my_set_)

    print("======================testing strings ==========================")
    print("==>ft_filter(filter_b, my_stri)")
    print(ft_filter(filter_b, my_stri))

    print("==>ft_filter(even, '""')")
    print(ft_filter(even, ""))

    print("==>ft_filter(lambda x: x > '3', my_stri)")
    print(ft_filter(lambda x: x > '3', my_stri))
    for elem in ft_filter(lambda x: x > '3', my_stri):
        print(elem)
    print("Original Set ==>", my_stri)  

    print("==>ft_filter(filter_b, '""')")
    print(ft_filter(even, ""))
    print("======================testing tuples ==========================")
    print("==>ft_filter(filter_b, (1, 2, 3, 4, 5, 'b', 7, 8, 9, 10)")
    print(ft_filter(filter_b, (1, 2, 3, 4, 5, 'b', 7, 8, 9, 10)))

    print("==>ft_filter(filter_b, my_tupl)")
    print(ft_filter(filter_b, my_tupl))
    print("==>ft_filter(even, my_tupl)")
    print(ft_filter(even, my_tupl))

    print("==>ft_filter(filter_b, tuple())")
    print(ft_filter(even, tuple()))
    print("======================testing dictionaries =====================")
    print("==>ft_filter(filter_b,\
           {1: 1,2: 2,3: 3,4: 4,5: 'b',6: 6,7: 7,8: 8,9: 9,10: 10}")
    print(ft_filter(filter_b,
                    {1: 1, 2: 2, 3: 3, 4: 4, 5: 'b',
                    6: 6, 7: 7, 8: 8, 9: 9, 10: 10}
                    ))

    print("==>ft_filter(filter_b, my_tupl)")
    print(ft_filter(filter_b, my_dict))
    print("==>ft_filter(even, my_tupl)")
    print(ft_filter(even, my_dict))

    print("==>ft_filter(filter_b, tuple())")
    print(ft_filter(even, dict()))



#if __name__ == '__main__':
    print("="*80)
    print("\t\t\t\t\tProbando ft_map")
    print("="*80)

    my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    my_set_ = set(my_list)
    my_tupl = tuple(my_list)
    my_dict = {1: 1, 2: 2, 3: 3, 4: 4, 5: 5, 6: 6, 7: 7, 8: 8, 9: 9, 10: 10}
    my_stri = "1234b67890"

    def duplicate(elem):
        return elem * 2

    def triplicate(elem):
        return elem * 3

    print("======================testing Extrem cases =====================")
    print("==>ft_map(None,  None)")
    print(ft_map(None, None))
    for elem in ft_map(None,  None):
        print(elem)

    print("==>ft_map(duplicate, None)")
    print(ft_map(duplicate, None))
    for elem in ft_map(duplicate,  None):
        print(elem)

    print("==>ft_map(None,  my_list)")
    print(ft_map(None,  my_list))
    for elem in ft_map(None,  my_list):
        print(elem)

    print("==>ft_map(my_dict,  my_list)")
    print(ft_map(my_dict,  my_list))
    for elem in ft_map(my_dict,  my_list):
        print(elem)

    print("======================testing list ==========================")
    print("==>ft_map(triplicate,  my_list)")
    print(ft_map(triplicate, my_list))
    for elem in ft_map(triplicate,  my_list):
        print(elem)
    print("Original list ==>",  my_list)
    print("==>ft_map(duplicate, my_list)")
    print(ft_map(duplicate, my_list))
    for elem in ft_map(duplicate,  my_list):
        print(elem)
    print("Original list ==>",  my_list)
    print("==>ft_map(duplicate,  [])")
    print(ft_map(duplicate,  []))
    for elem in ft_map(duplicate,  []):
        print(elem)
    print("======================testing sets ==========================")
    print("==>ft_map(triplicate,  ()))")
    print(ft_map(triplicate,  set()))
    for elem in ft_map(triplicate,  set()):
        print(elem)
    print("==>ft_map(duplicate,  my_set_)")
    print(ft_map(duplicate,  my_set_))
    for elem in ft_map(duplicate,  my_set_):
        print(elem)
    print("Original set ==>",  my_set_)
    print("==>ft_map(duplicate, [])")
    print(ft_map(duplicate, set()))
    for elem in ft_map(duplicate, set()):
        print(elem)

    print("======================testing strings ==========================")
    print("==>ft_map(triplicate,  my_stri)")
    print(ft_map(triplicate,  my_stri))
    for elem in ft_map(triplicate,  my_stri):
        print(elem)
    print("Original string ==>",  my_stri)

    print("==>ft_map(duplicate,  '""')")
    print(ft_map(duplicate,  ""))
    for elem in ft_map(duplicate,  ""):
        print(elem)
    print("==>ft_map(duplicate,  my_stri)")
    print(ft_map(duplicate,  my_stri))
    for elem in ft_map(duplicate,  my_stri):
        print(elem)
    print("Original string ==>",  my_stri)
    print("==>ft_map(triplicate,  '""')")
    print(ft_map(duplicate,  ""))
    for elem in ft_map(duplicate,  ""):
        print(elem)

    print("======================testing tuples ==========================")
    print("==>ft_map(triplicate,  (1,  2,  3,  4,  5,  'b',  7,  8,  9,  10)")
    print(ft_map(triplicate,  (1, 2, 3, 4, 5, 'b', 7, 8, 9, 10)))
    for elem in ft_map(triplicate,  (1, 2, 3, 4, 5, 'b', 7, 8, 9, 10)):
        print(elem)

    print("==>ft_map(triplicate,  my_tupl)")
    print(ft_map(triplicate,  my_tupl))
    for elem in ft_map(triplicate,  my_tupl):
        print(elem)
    print("Original tup ==>",  my_tupl)

    print("==>ft_map(duplicate,  my_tupl)")
    print(ft_map(duplicate,  my_tupl))
    for elem in ft_map(duplicate,  my_tupl):
        print(elem)
    print("Original tup ==>",  my_tupl)

    print("==>ft_map(triplicate,  tuple())")
    print(ft_map(duplicate,  tuple()))
    for elem in ft_map(duplicate,  ""):
        print(elem)

    print("======================testing dictionaries =======================")
    print("==>ft_map(triplicate,{1: 1, 2: 2, 3: 3, 4: 4, 5: 'b', 6: 6, \
          7: 7, 8: 8, 9: 9, 10: 10}")
    print(ft_map(triplicate,
                 {1: 1, 2: 2, 3: 3, 4: 4, 5: 'b', 6: 6, 7: 7,
                  8: 8, 9: 9, 10: 10}))
    for elem in ft_map(triplicate,
                       {1: 1, 2: 2, 3: 3, 4: 4, 5: 'b', 6: 6,
                        7: 7, 8: 8, 9: 9, 10: 10}):
        print(elem)

    print("==>ft_map(triplicate,  my_dict)")
    print(ft_map(triplicate,  my_dict))
    for elem in ft_map(triplicate,  my_dict):
        print(elem)
    print("Original dict ==>",  my_dict)

    print("==>ft_map(duplicate,  my_dict)")
    print(ft_map(duplicate,  my_dict))
    for elem in ft_map(duplicate,  my_dict):
        print(elem)
    print("Original dict ==>",  my_dict)

    print("==>ft_map(triplicate,  dict())")
    print(ft_map(duplicate,  dict()))
    for elem in ft_map(duplicate,  dict()):
        print(elem)

    print("="*80)
    print("\t\t\t\t\tProbando ft_reduce")
    print("="*80)
    print("="*80)
    print("\t\t\t\t\tProbando ft_reduce")
    print("="*80)

    my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    my_set_ = set(my_list)
    my_tupl = tuple(my_list)
    my_dict = {1: 1, 2: 2, 3: 3, 4: 4, 5: 5, 6: 6, 7: 7, 8: 8, 9: 9, 10: 10}
    my_stri = "1234b67890"

    def even(elem):
        return (elem % 2 == 0)

    print("======================testing Extrem cases ====================")
    print("==>ft_reduce(None, None)")
    print(ft_reduce(None, None))

    print("==>ft_reduce(even, None)")
    print(ft_reduce(even, None))

    print("==>ft_reduce(None, my_list)")
    print(ft_reduce(None, my_list))

    print("==>ft_reduce(my_dict, my_list)")
    print(ft_reduce(my_dict, my_list ))
    print("======================testing lists ====================")

    
    print("ft_reduce(lambda u, v: u + v, my_list)")
    print(ft_reduce(lambda u, v: u + v, my_list), type(ft_reduce(lambda u, v: u + v, my_list)))
    print("Original list ==>", type(my_list), " of ", type(my_list[0]), my_list)

    print("ft_reduce(lambda u, v: u + v, set(['a', 'b', 'c']))")
    print(ft_reduce(lambda u, v: u + v, ['a', 'b', 'c']), type(ft_reduce(lambda u, v: u + v, ['a', 'b', 'c'])))
    print("Original list ==>", type(['a', 'b', 'c']), " of ", type(['a', 'b', 'c'][0]), ['a', 'b', 'c'])

    print("======================testing sets ====================")


    print("ft_reduce(lambda u, v: u + v, my_set_)")
    print(ft_reduce(lambda u, v: u + v, my_set_), type(ft_reduce(lambda u, v: u + v, my_set_)))
    print("Original list ==>", type(my_set_), " of ", type(list(my_set_)[0]), my_set_)
    print("ft_reduce(lambda u, v: u + v, set(('a', 'b', 'c')))")
    print(ft_reduce(lambda u, v: u + v, set(('a', 'b', 'c'))), type(ft_reduce(lambda u, v: u + v, set(('a', 'b', 'c')))))    
    print("Original list ==>", type(set(('a', 'b', 'c'))), " of ", type(list(set(('a', 'b', 'c')))[0]),set(('a', 'b', 'c')))

    print("======================testing tuples ====================")

    
    print("ft_reduce(lambda u, v: u + v, my_tuple)")
    print(ft_reduce(lambda u, v: u + v, my_tupl), type(ft_reduce(lambda u, v: u + v, my_tupl)))
    print("Original list ==>", type(my_tupl)," of ", type(my_tupl[0]), my_tupl)

    print("ft_reduce(lambda u, v: u + v, ('a', 'b', 'c'))")
    print(ft_reduce(lambda u, v: u + v, ('a', 'b', 'c')), type(ft_reduce(lambda u, v: u + v, ('a', 'b', 'c'))))    
    print("Original list ==>", type(('a', 'b', 'c')), " of ", type(('a', 'b', 'c')[0]),('a', 'b', 'c'))

    print("======================testing Dictionaries ====================")

    
    print("ft_reduce(lambda u, v: u + v, my_dict)")
    print(ft_reduce(lambda u, v: u + v, my_dict), type(ft_reduce(lambda u, v: u + v, my_dict)))
    print("Original list ==>", type(my_dict), "of ", type(list(my_dict.values())[0]),my_dict)
    
    my_dict ={1: 'a', 2: '2', 3: '3', 4: '4', 5: 'c', 6: '6', 7: '7', 8: '8', 9: '9', 10: 't'}
    print("ft_reduce(lambda u, v: u + v, my_dict)")
    print(ft_reduce(lambda u, v: u + v, my_dict), type(ft_reduce(lambda u, v: u + v, my_dict)))
    print("Original list ==>", type(my_dict), "of ", type(list(my_dict.values())[0]),my_dict)
    
    print("======================Probando Subject Cases ==============")
    lst = ['H', 'e', 'l', 'l', 'o', ' ', 'w', 'o', 'r', 'l', 'd']
    print("ft_reduce(lambda u, v: u + v, lst)")
    print(ft_reduce(lambda u, v: u + v, lst), type(ft_reduce(lambda u, v: u + v, lst)))
    print("Original list ==>", type(lst), " of ", type(lst[0]),lst)

    """
    my_set ={1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
    print("Original list ==>", type(my_set_), my_set_)
    print(reduce(lambda x,y: x+y, my_set_), type(reduce(lambda x,y: x+y, my_set_)))
    print("Original list ==>", type(('a', 'b','c')), ('a', 'b','c'))
    print(reduce(lambda x,y: x+y, ('a', 'b','c')), type(reduce(lambda x,y: x+y, ('a', 'b','c'))))
    """
    print("="*80)
    print("\t\t\t\t\tProbando Subject Cases")
    print("="*80)

    print("# Example 1")
    x = [1, 2, 3, 4, 5]
    print("print(ft_map(lambda dum: dum + 1, x))")
    print(ft_map(lambda dum: dum + 1, x))
    for elem in ft_map(lambda dum: dum + 1, x):
        print(elem)
    list(ft_map(lambda t: t + 1, x))

    print("# Example 2:")
    print("ft_filter(lambda dum: not (dum % 2), x)")
    print(ft_filter(lambda dum: not (dum % 2), x))
    for elem in ft_filter(lambda dum: not (dum % 2), x):
        print(elem)
    list(ft_filter(lambda dum: not (dum % 2), x))
    # Output:
    [2, 4]
    print("# Example 3:")
    lst = ['H', 'e', 'l', 'l', 'o', ' ', 'w', 'o', 'r', 'l', 'd']
    print("ft_reduce(lambda u, v: u + v, lst)")
    print(ft_reduce(lambda u, v: u + v, lst))
    # Output:
    "Hello world"
    