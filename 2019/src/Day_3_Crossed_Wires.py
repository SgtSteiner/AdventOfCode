"""
Enunciado del problema: https://adventofcode.com/2019/day/3

"""

import os

def calc_path_wire(wire):
     coord = []
     x = y = 0
     for move in wire:
          direction = move[0]
          dist = int(move[1:])
          for _ in range(dist):
               if direction == "R":
                    x += 1
               elif direction == "L":
                    x -= 1
               elif direction == "U":
                    y += 1
               elif direction == "D":
                    y -= 1
               coord.append((x, y))
     return coord

# Lectura del archivo de datos
filePath = os.path.relpath('../data/input_day03.txt')
with open(filePath,'r') as f:
     data = f.readlines()

data = [item.rstrip('\n') for item in data]

#--- Part 1 ---
paths = [calc_path_wire(wire.split(",")) for wire in data]
crossed = set.intersection(*map(set, paths))  # wire intersection
cross_min = min([abs(cross[0]) + abs(cross[1]) for cross in crossed])
print(f"El resultado de la parte 1: {cross_min}")

#--- Part 2 ---
steps = [sum([path.index(cross) + 1 for path in paths]) for cross in crossed]
print(f"El resultado de la parte 2: {min(steps)}")
