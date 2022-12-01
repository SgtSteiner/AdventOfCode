"""
--- Day 8: Matchsticks ---
http://adventofcode.com/2015/day/8
"""

import sys
import re

puzzle_data = sys.stdin.readlines()

total_char_string_code = 0
total_char_memory_one = 0
total_char_memory_two = 0

for line in puzzle_data:
    santa_line = line.strip()
    total_char_string_code += len(santa_line)
    santa_line = santa_line[1:-1]
    santa_line = re.sub(r'\\x[0-9a-f]{2}', 'Z', santa_line)
    santa_line = re.sub(r'\\"', '"', santa_line)
    santa_line = re.sub(r'\\\\', 'B', santa_line)
    total_char_memory_one += len(santa_line)

for line in puzzle_data:
    santa_line = line.strip()
    santa_line = re.sub(r'\\', '\\\\\\\\', santa_line)
    santa_line = re.sub(r'"', '\\"', santa_line)
    santa_line = '"' + santa_line + '"'
    total_char_memory_two += len(santa_line)

print("Total part one: {0}".format(total_char_string_code - total_char_memory_one))
print("Total part two: {0}".format(total_char_memory_two - total_char_string_code))