#!/usr/local/bin/python3
from TinyStatistician import TinyStatistician
import numpy as np


stat = TinyStatistician()

# stat.valid([1, 2, 3, 4, 5, 'b', 6, 7])

a = np.array([1, 2, 3, 4, 5, 9, 6, 7])

print(stat.valid(a))

a = [1, 42, 300, 10, 59]
print("Mean:", stat.mean(a))
print("Median", stat.median(a))
print("Quartiles", stat.quartiles(a))
print("var", stat.var(a))
print("std", stat.std(a))
