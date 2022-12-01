"""
Enunciado del problema: https://adventofcode.com/2019/day/1

"""

import os

def calc_fuel(mass, additional=True):
    fuel = (mass // 3) - 2
    if additional:
        return fuel + calc_fuel(fuel) if fuel > 0 else 0
    else:
        return fuel if fuel > 0 else 0


# Lectura del archivo de datos
filePath = os.path.relpath('../data/input_day01.txt')
with open(filePath,'r') as f:
     data = f.readlines()
data = [int(item.rstrip('\n')) for item in data]

# --- Part 1 ---
total_fuel = sum(calc_fuel(mass, additional=False) for mass in data)
print(f"Resultado parte 1: {total_fuel}")

# --- Part 2 ---
total_fuel = sum(calc_fuel(mass) for mass in data)
print(f"Resultado parte 2: {total_fuel}")

