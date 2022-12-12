"""_summary_: https://adventofcode.com/2022/day/4

"""

import string

# Lee archivo de entrada
def read_input():
    with open("input.txt", 'r') as f:
        return f.readlines()
    
    
if __name__ == "__main__":
    assignments  = [item.rstrip('\n').split(",") for item in read_input()]
    """ assignments = [
        "2-4,6-8".split(","),
        "2-3,4-5".split(","),
        "5-7,7-9".split(","),
        "2-8,3-7".split(","),
        "6-6,4-6".split(","),
        "2-6,4-8".split(","),
    ] """
    
    total_fully_contain = 0
    total_ranges_overlap = 0
    for assignment in assignments:
        first_elve, second_elve = assignment[0].split("-"), assignment[1].split("-")
        first_elve_start, first_elve_end = map(int, assignment[0].split("-"))
        second_elve_start, second_elve_end = map(int, assignment[1].split("-"))
        
        if (first_elve_start <= second_elve_start and second_elve_end <= first_elve_end) or \
            (second_elve_start <= first_elve_start and first_elve_end <=second_elve_end):
            total_fully_contain += 1
            
        if set(range(first_elve_start, first_elve_end + 1)).intersection(set(range(second_elve_start, second_elve_end + 1))):
            total_ranges_overlap += 1
                        
    print(total_fully_contain)
    print(total_ranges_overlap)
    