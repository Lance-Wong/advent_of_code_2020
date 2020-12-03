import itertools
import numpy as np

inputs= '''https://adventofcode.com/2020/day/1/input'''
inputs = [int(x) for x in inputs.split('\n')]

combinations =3
# toggle for pt1 and pt2

for i in itertools.combinations(inputs,combinations):
    if sum(i) == 2020:
        print(np.prod(i))
        break
    else:
        pass
