"""_summary_: https://adventofcode.com/2022/day/8

"""

# Lee archivo de entrada
def read_input():
    with open("input.txt", 'r') as f:
        return f.readlines()
    
def is_tree_visible(data, row, col):
    tree = data[row][col]
    
    # verify up
    is_visible = True
    for i in range(0, row):
        if data[i][col] >= tree:
            is_visible = False
    if is_visible:
        return is_visible
            
    # verify down
    is_visible = True
    for i in range(row+1, len(data)):
        if data[i][col] >= tree:
            is_visible = False
    if is_visible:
        return is_visible
        
    # verify left
    is_visible = True
    for i in range(0, col) :
        if data[row][i] >= tree:
            is_visible = False
    if is_visible:
        return is_visible
        
    # verify right
    is_visible = True
    for i in range(col+1, len(data)) :
        if data[row][i] >= tree:
            is_visible = False
    if is_visible:
        return is_visible
    
def calc_tree_scenic(data, row, col):
    tree = data[row][col]
    tree_scenic_score = 0
    
    # verify up
    trees = 0
    for i in reversed(range(0, row)):
        trees += 1
        if data[i][col] >= tree:
            break
    tree_scenic_score = trees
        
    # verify down
    trees = 0
    for i in range(row+1, len(data)):
        trees += 1
        if data[i][col] >= tree:
            break
    tree_scenic_score *= trees
        
    # verify left
    trees = 0
    for i in reversed(range(0, col)) :
        trees += 1
        if data[row][i] >= tree:
            break
    tree_scenic_score *= trees
        
    # verify right
    trees = 0
    for i in range(col+1, len(data)) :
        trees += 1
        if data[row][i] >= tree:
            break
    tree_scenic_score *= trees
        
    return tree_scenic_score


if __name__ == "__main__":
    data  = [item.rstrip('\n') for item in read_input()]
    
    size = (len(data) * 4) - 4  # árboles de los bordes
    max_tree_scenic_score = 0

    for row in range(1, len(data)-1):
        for col in range(1, len(data[row])-1):
            
            if is_tree_visible(data, row, col):
                size += 1
            
            tree_scenic_score = calc_tree_scenic(data, row, col)
            if tree_scenic_score > max_tree_scenic_score:
                max_tree_scenic_score = tree_scenic_score
        
    print(f"Part one: {size}")
    print(f"Part two: {max_tree_scenic_score}")
