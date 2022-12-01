"""
Enunciado del problema: https://adventofcode.com/2020/day/5

"""

import os

# Read datafile
filePath = os.path.relpath('../data/input_day06.txt')
with open(filePath,'r') as f:
     data = f.read().split("\n\n")

group_forms = [element.replace("\n", " ").split() for element in data]

# --- Part 1 ---
questions = [len(set("".join(group))) for group in group_forms]
print(f"El resultado de la parte 1: {sum(questions)}")

# --- Part 2 ---
questions = [len(set.intersection(*map(set, group))) for group in group_forms]
print(f"El resultado de la parte 2: {sum(questions)}")
