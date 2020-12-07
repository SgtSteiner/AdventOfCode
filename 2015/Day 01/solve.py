def read_input():
    # Lectura del archivo de datos
    with open("input.txt", 'r') as f:
        return list(f.read())


def calc_floor(data):
    return data.count("(") - data.count(")")


def call_basement(data):
    floor = 0
    position = 0
    for element in data:
        position += 1
        if element == "(":
            floor += 1
        else:
            floor -= 1
        if floor < 0:
            return position


if __name__ == "__main__":
    datos = read_input()

    # print the floor
    print(f"Part1 - Floor: {calc_floor(datos)}")

    # print the position of the character that causes Santa to first enter the basement
    print(f"Part2 - Position basement: {call_basement(datos)}")
