"""_summary_: https://adventofcode.com/2022/day/6

"""

# Lee archivo de entrada
def read_input():
    with open("input.txt", 'r') as f:
        return f.readlines()
    
def find_marker(size_marker):
    pos_ini = 0
    pos_end = size_marker
    while pos_end <= len(data):
        if len(set(data[pos_ini:pos_end])) == size_marker:
            return pos_end
        pos_ini += 1
        pos_end += 1
        
    
if __name__ == "__main__":
    data  = list([item.rstrip('\n') for item in read_input()][0])
        
    print(f"Part one = {find_marker(4)}")
    print(f"Part two = {find_marker(14)}")
    