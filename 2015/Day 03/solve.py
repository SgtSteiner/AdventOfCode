def read_input():
    # Read input data
    with open("input.txt", 'r') as f:
        return list(f.read())


def move_house(rumbo, x_coord, y_coord):
    if rumbo == "^":
        y_coord += 1
    elif rumbo == "v":
        y_coord -= 1
    elif rumbo == ">":
        x_coord += 1
    elif rumbo == "<":
        x_coord -= 1
    return x_coord, y_coord


def house_santa(moves):
    houses = [(0, 0)]  # Se inicia la ruta en las coordenadas (0, 0)
    x_santa = y_santa = 0
    for move in moves:
        x_santa, y_santa = move_house(move, x_santa, y_santa)
        houses.append((x_santa, y_santa))
    return len(set(houses))


def house_robosanta(moves):
    houses = [(0, 0)]  # Se inicia la ruta en las coordenadas (0, 0)
    x_santa = y_santa = x_robo = y_robo = 0
    movement = 0
    for move in moves:
        movement += 1
        if movement % 2 != 0:
            x_santa, y_santa = move_house(move, x_santa, y_santa)
            houses.append((x_santa, y_santa))
        else:
            x_robo, y_robo = move_house(move, x_robo, y_robo)
            houses.append((x_robo, y_robo))
    return len(set(houses))


if __name__ == "__main__":
    datos = read_input()

    print(f"Total houses Santa: {house_santa(datos)}")
    print(f"Total houses Robo Santa: {house_robosanta(datos)}")
