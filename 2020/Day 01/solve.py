from itertools import combinations
import numpy as np


def read_input():
    with open("input.txt", 'r') as f:
        return f.readlines()


def suma_tupla(data, entries=2, suma=2020):
    perm = combinations(data, entries)
    for tupla in perm:
        if sum(tupla) == suma:
            return np.prod(np.array(tupla))
    return None


if __name__ == "__main__":
    data = [int(item.rstrip('\n')) for item in read_input()]

    print(f"Part 1: {suma_tupla(data, entries=2)}")
    print(f"Part 2: {suma_tupla(data, entries=3)}")

    print(data)
