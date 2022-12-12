"""_summary_: https://adventofcode.com/2022/day/5

"""

import pickle

original_stacks = pickle.dumps([
        ["Q", "M", "G", "C", "L"],
        ["R", "D", "L", "C", "T", "F", "H", "G"],
        ["V", "J", "F", "N", "M", "T", "W", "R"],
        ["J", "F", "D", "V", "Q", "P"],
        ["N", "F", "M", "S", "L", "B", "T"],
        ["R", "N", "V", "H", "C", "D", "P"],
        ["H","C", "T"],
        ["G", "S", "J", "V", "Z", "N", "H", "P"],
        ["Z", "F", "H", "G"],
    ])

# Lee archivo de entrada
def read_input():
    with open("input.txt", 'r') as f:
        return f.readlines()
    
if __name__ == "__main__":
    data  = [item.rstrip('\n') for item in read_input()]
    
    stacks_part_one = pickle.loads(original_stacks)
    stacks_part_two = pickle.loads(original_stacks)
    for item in data[10:]:
        movement = item.split(" ")
        quantity = int(movement[1])
        from_stack = int(movement[3])
        to_stack = int(movement[5])
        
        # Part one
        for i in range(quantity):
            stacks_part_one[to_stack-1].append(stacks_part_one[from_stack-1].pop())
        
        # Part two
        for crate in stacks_part_two[from_stack-1][quantity*(-1):]:
            stacks_part_two[to_stack-1].append(crate)
            stacks_part_two[from_stack-1].pop()
        
    part_one = "".join([stack[-1] for stack in stacks_part_one])
    print(part_one)
    
    part_two = "".join([stack[-1] for stack in stacks_part_two])
    print(part_two)
    
