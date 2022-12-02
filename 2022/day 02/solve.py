"""_summary_: https://adventofcode.com/2022/day/2

"""

# Puntuación de cada forma
shape_score = {
    "X": 1,
    "Y": 2,
    "Z": 3
}

# Puntuación según el resultado de la partida
round_score = {
    "gano": 6,
    "empato": 3,
    "pierdo": 0
}    

# Combinaciones en las que ganas
round_victory = {
    "A": "Y",
    "B": "Z",
    "C": "X",
}
# Combinaciones en las que empatas
round_draw = {
    "A": "X",
    "B": "Y",
    "C": "Z",
}
# Combinaciones en las que pierdes
round_defeat = {
    "A": "Z",
    "B": "X",
    "C": "Y",
}

# Lee archivo de entrada
def read_input():
    with open("input.txt", 'r') as f:
        return f.readlines()
    
# Calcula el resultado de cada partida - Parte 1
def calc_score_round_part_one(data):
    total_score = 0
    for round_shapes in data:        
        if round_victory[round_shapes[0]] == round_shapes[1]:
            result_score = "gano"
        elif round_draw[round_shapes[0]] == round_shapes[1]:
            result_score = "empato"
        else:
            result_score = "pierdo"
        total_score += shape_score[round_shapes[1]] + round_score[result_score]
    return total_score

# Calcula el resultado de cada partida - Parte 2
def calc_score_round_part_two(data):
    total_score = 0
    for round_shapes in data:        
        # Tengo que ganar
        if round_shapes[1] == "Z":
            shape = round_victory[round_shapes[0]]
            result_score = "gano"
        # Tengo que empatar
        elif round_shapes[1] == "Y":
            shape = round_draw[round_shapes[0]]
            result_score = "empato"
        # Tengo que perder
        else:
            shape = round_defeat[round_shapes[0]]
            result_score = "pierdo"
        total_score += shape_score[shape] + round_score[result_score]
    return total_score

if __name__ == "__main__":
    data = [item.rstrip('\n').split() for item in read_input()]
    
    part_one = calc_score_round_part_one(data)
    print(f"Part 1 - Total score: {part_one}")
    
    part_two = calc_score_round_part_two(data)
    print(f"Part 2 - Total score: {part_two}")
