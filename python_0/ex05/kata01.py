#!/usr/bin/python3
kata = {
        'Python': 'Guido van Rossum',
        'Ruby': 'Yukihiro Matsumoto',
        'PHP': 'Rasmus Lerdorf',
        }
kata = {}
if kata != {}:
    for k, v in kata.items():
        print("{} was created by {}".format(k, v))
else:
    print("En empty diccionary outputs nothing")
