"""_summary_: https://adventofcode.com/2022/day/9

"""

    
# Lee archivo de entrada
def read_input():
    with open("input.txt", 'r') as f:
        return f.readlines()
    
def calc_tail_position(head_row, head_col, tail_row, tail_col):
    if head_row == tail_row:  # same row
        if head_col - tail_col == 2:    # two step right then move tail right
            tail_col += 1
        elif head_col - tail_col == -2: # two step left then move tail left
            tail_col -= 1
        
    elif head_col == tail_col: # same col
        if head_row - tail_row == 2:    # two step up then move tail up
            tail_row += 1
        elif head_row - tail_row == -2: # two step down then move tail down
            tail_row -= 1
            
    elif abs(head_row - tail_row) == 2: # separated two rows
        if head_row > tail_row:
            tail_row += 1
            tail_col = head_col
        else:
            tail_row -= 1
            tail_col = head_col
            
    elif abs(head_col - tail_col) == 2: # separated two cols
        if head_col > tail_col:
            tail_col += 1
            tail_row = head_row
        else:
            tail_col -= 1
            tail_row = head_row
    
    return tail_row, tail_col

if __name__ == "__main__":
    data  = [item.rstrip('\n') for item in read_input()]
    
    # Part ONE
    tail_locations = [(0,0)]
    head_row = 0
    head_col = 0
    tail_row = 0
    tail_col = 0
    
    for motion in data:
        direction, steps = motion.split()
        for _ in range(int(steps)):
            if direction == "R":
                head_col += 1
            elif direction == "L":
                head_col -= 1
            elif direction == "U":
                head_row += 1
            else:
                head_row -= 1
            tail_row, tail_col = calc_tail_position(head_row, head_col, tail_row, tail_col)
            if (tail_row, tail_col) not in tail_locations:
                tail_locations.append((tail_row, tail_col))
                
    print(f"Part one: {len(tail_locations)}")
    
    # Part TWO
    head_row = 0
    head_col = 0
    num_knots = 10
    knots = {}
    for i in range(num_knots):
        knots[i] = {
            "tail_locations": [(0,0)],
            "row": 0,
            "col": 0,
        }
    
    
    for motion in data:
        direction, steps = motion.split()
        for _ in range(int(steps)):
            if direction == "R":
                head_col += 1
            elif direction == "L":
                head_col -= 1
            elif direction == "U":
                head_row += 1
            else:
                head_row -= 1
            
            knots[0]["row"] = head_row
            knots[0]["col"] = head_col
            for i in range(num_knots-1):
                knots[i+1]["row"], knots[i+1]["col"] = calc_tail_position(
                                                                            knots[i]["row"], 
                                                                            knots[i]["col"], 
                                                                            knots[i+1]["row"], 
                                                                            knots[i+1]["col"]
                                                                        )
                if (knots[i+1]["row"], knots[i+1]["col"]) not in knots[i+1]["tail_locations"]:
                    knots[i+1]["tail_locations"].append((knots[i+1]["row"], knots[i+1]["col"]))                
                    
    print(f'Part two: {len(knots[num_knots-1]["tail_locations"])}')
