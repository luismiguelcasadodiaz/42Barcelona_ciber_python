#!/usr/bin/python3
from time import sleep
from loading import ft_progress

def test_x(X):
    ret = 0
    for elem in ft_progress(X):
        ret = ret + (elem + 3) % 5
        sleep(0.01)
    print()
    print(ret)



X = range(100)
test_x(X)
X = range(100, 200)
test_x(X)
X = range(1)
test_x(X)
X = range(4)
test_x(X)
X = range(0, -100, -1)
test_x(X)
