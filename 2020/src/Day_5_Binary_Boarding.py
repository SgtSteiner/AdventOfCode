"""
Enunciado del problema: https://adventofcode.com/2020/day/5

"""

import os

def calc_seat(boarding_pass):
    seat_rows = list(range(128))
    seat_cols = list(range(8))

    rows = boarding_pass[:7]
    cols = boarding_pass[7:]
    
    for row in rows:
        if row == "F":
            seat_rows = seat_rows[:len(seat_rows)//2]
        else:
            seat_rows = seat_rows[len(seat_rows)//2:]

    for col in cols:
        if col == "L":
            seat_cols = seat_cols[:len(seat_cols)//2]
        else:
            seat_cols = seat_cols[len(seat_cols)//2:]
    
    return seat_rows[0] * 8  + seat_cols[0]

# Read datafile
filePath = os.path.relpath('../data/input_day05.txt')
with open(filePath,'r') as f:
     data = f.readlines()
data = [item.rstrip('\n') for item in data]

# --- Part 1 ---
seats = [calc_seat(boarding_pass) for boarding_pass in data]
print(f"Resultado parte 1: {max(seats)}")

# --- Part 2 ---
my_seat = [seat for seat in range(min(seats), max(seats)+1) if seat not in(seats)]
print(f"Resultado parte 2: {my_seat[0]}")