from itertools import permutations
import math

with open('puzzle_input_data.txt', 'r') as datafile:
    dataset = datafile.read()
    dataset = list(dataset.split('\n'))
    del dataset[-1]

    combinations = list(permutations(dataset, 3))# for part one change to 2i

    valid_2020s = [ i for i in combinations if sum([int(x) for x in list(i)]) == 2020]

    print([math.prod(list([int(x) for x in i])) for i in valid_2020s])

