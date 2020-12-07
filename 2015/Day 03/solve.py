"""
--- Day 3: Perfectly Spherical Houses in a Vacuum ---

Santa is delivering presents to an infinite two-dimensional grid of houses.

He begins by delivering a present to the house at his starting location,
and then an elf at the North Pole calls him via radio and tells him where to move next.
Moves are always exactly one house to the north (^), south (v), east (>), or west (<).
After each move, he delivers another present to the house at his new location.

However, the elf back at the north pole has had a little too much eggnog,
and so his directions are a little off, and Santa ends up visiting some houses more than once.
How many houses receive at least one present?

For example:

. > delivers presents to 2 houses: one at the starting location, and one to the east.
. ^>v< delivers presents to 4 houses in a square, including twice to the house at his starting/ending location.
. ^v^v^v^v^v delivers a bunch of presents to some very lucky children at only 2 houses.

--- Part Two ---

The next year, to speed up the process, Santa creates a robot version of himself, Robo-Santa,
to deliver presents with him.

Santa and Robo-Santa start at the same location (delivering two presents to the same starting house),
then take turns moving based on instructions from the elf, who is eggnoggedly reading from the same
script as the previous year.

This year, how many houses receive at least one present?

For example:

. ^v delivers presents to 3 houses, because Santa goes north, and then Robo-Santa goes south.
. ^>v< now delivers presents to 3 houses, and Santa and Robo-Santa end up back where they started.
. ^v^v^v^v^v now delivers presents to 11 houses, with Santa going one direction and Robo-Santa going the other.
"""


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


datos = list(input())

""" --- Part One --- """
houses = [(0, 0)]           # Se inicia la ruta en las coordenadas (0, 0)
x_santa = y_santa = 0
for dato in datos:
    x_santa, y_santa = move_house(dato, x_santa, y_santa)
    houses.append((x_santa, y_santa))

print("Total houses: {0}".format(len(set(houses))))

""" --- Part Two --- """
houses = [(0, 0)]           # Se inicia la ruta en las coordenadas (0, 0)
x_santa = y_santa = x_robo = y_robo = 0
movement = 0
for dato in datos:
    movement += 1
    if movement % 2 != 0:
        x_santa, y_santa = move_house(dato, x_santa, y_santa)
        houses.append((x_santa, y_santa))
    else:
        x_robo, y_robo = move_house(dato, x_robo, y_robo)
        houses.append((x_robo, y_robo))

print("Total houses Robo-Santa: {0}".format(len(set(houses))))
