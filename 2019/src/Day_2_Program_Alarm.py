"""
Enunciado del problema: https://adventofcode.com/2019/day/2

"""

import os
from itertools import product

def restore_data(data, noun, verb):
     data_program = data.copy()
     data_program[1] = noun
     data_program[2] = verb
     for pointer in range(0, len(data_program), 4):
          opcode = data_program[pointer]
          numberA = data_program[data_program[pointer + 1]]
          numberB = data_program[data_program[pointer + 2]]
          if opcode == 1:
               data_program[data_program[pointer + 3]] = numberA + numberB
          elif opcode == 2:
               data_program[data_program[pointer + 3]] = numberA * numberB
          elif opcode == 99:
               return data_program
     return data_program


# Lectura del archivo de datos
filePath = os.path.relpath('../data/input_day02.txt')
with open(filePath,'r') as f:
     data = f.read().rstrip()
data = list(map(int, data.split(",")))

# --- Part 1 ---
noun = 12
verb = 2
data_program = restore_data(data, noun, verb)
print(f"Resultado de la parte 1: {data_program[0]}")

# --- Part 2 ---
output = 19690720
for noun, verb in tuple(product(range(100), repeat=2)):
     data_program = restore_data(data, noun, verb)
     if data_program[0] == output:
          print(f"Resultado de la parte 2: {100 * noun + verb}")
          break




