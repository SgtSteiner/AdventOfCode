"""_summary_: https://adventofcode.com/2022/day/3

"""

import string

# Lee archivo de entrada
def read_input():
    with open("input.txt", 'r') as f:
        return f.readlines()
    
def calc_item_type(rucksacks):
    total_sum = 0
    for rucksack in rucksacks:
        first_half = rucksack[:len(rucksack)//2]
        second_half = rucksack[len(rucksack)//2:]
        item_type = set(first_half).intersection(second_half)
        total_sum += string.ascii_letters.find(list(item_type)[0]) + 1
    return total_sum

def calc_item_type_badge(rucksacks):
    total_sum = 0
    for i in range(0, len(rucksacks), 3):
        item_type = set(rucksacks[i]).intersection(rucksacks[i+1], rucksacks[i+2])
        total_sum += string.ascii_letters.find(list(item_type)[0]) + 1
    return total_sum
    
if __name__ == "__main__":
    data  = [item.rstrip('\n') for item in read_input()]
    
    print(f"Part one: {calc_item_type(data)}")
    print(f"Part two: {calc_item_type_badge(data)}")
