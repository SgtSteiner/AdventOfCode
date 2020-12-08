import numpy as np


def read_input():
    # read input data
    with open("input.txt", 'r') as f:
        return f.readlines()


def turn_lights(grid, action, row0, col0, row1, col1):
    """
    Actualiza la matriz de luces según las instrucciones y coordenadas
    """
    for row in range(row0, row1 + 1):
        for col in range(col0, col1 + 1):
            if action == "turn_on":
                grid[row][col] = 1
            elif action == "turn_off":
                grid[row][col] = 0
            elif action == "toggle":
                grid[row][col] = 1 - grid[row][col]


def turn_brightness(grid, action, row0, col0, row1, col1):
    """
    Actualiza la matriz de brillo según las instrucciones y coordenadas
    """
    for row in range(row0, row1 + 1):
        for col in range(col0, col1 + 1):
            if action == "turn_on":
                grid[row][col] += 1
            elif action == "turn_off":
                if grid[row][col] > 0:
                    grid[row][col] -= 1
            elif action == "toggle":
                grid[row][col] += 2


def read_instruction(instruction):
    instruction = instruction.split()
    col_start, row_start = list(map(int, instruction[-3].split(",")))
    col_end, row_end = list(map(int, instruction[-1].split(",")))
    action = instruction[0]
    if action == "turn":
        action += "_" + instruction[1]
    return action, row_start, col_start, row_end, col_end


def action_lights(instructions):
    grid = [[0] * 1000 for i in range(1000)]
    for instruction in instructions:
        action, row_start, col_start, row_end, col_end = read_instruction(instruction)
        turn_lights(grid, action, row_start, col_start, row_end, col_end)
    return np.sum(grid)


def action_brightness(instructions):
    grid = [[0] * 1000 for i in range(1000)]
    for instruction in instructions:
        action, row_start, col_start, row_end, col_end = read_instruction(instruction)
        turn_brightness(grid, action, row_start, col_start, row_end, col_end)
    return np.sum(grid)


if __name__ == "__main__":

    instructions = read_input()

    print(f"Part One - There are {action_lights(instructions)} lights on")
    print(f"Part Two - Total brightness are {action_brightness(instructions)}")
