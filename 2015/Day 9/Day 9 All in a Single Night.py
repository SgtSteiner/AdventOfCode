"""
--- Day 9: All in a Single Night ---

Every year, Santa manages to deliver all of his presents in a single night.

This year, however, he has some new locations to visit; his elves have provided him
the distances between every pair of locations. He can start and end at any two (different) locations he wants,
but he must visit each location exactly once. What is the shortest distance he can travel to achieve this?

For example, given the following distances:

London to Dublin = 464
London to Belfast = 518
Dublin to Belfast = 141
The possible routes are therefore:

Dublin -> London -> Belfast = 982
London -> Dublin -> Belfast = 605
London -> Belfast -> Dublin = 659
Dublin -> Belfast -> London = 659
Belfast -> Dublin -> London = 605
Belfast -> London -> Dublin = 982
The shortest of these is London -> Dublin -> Belfast = 605, and so the answer is 605 in this example.

What is the distance of the shortest route?

--- Part Two ---

The next year, just to show off, Santa decides to take the route with the longest distance instead.

He can still start and end at any two (different) locations he wants,
and he still must visit each location exactly once.

For example, given the distances above,
the longest route would be 982 via (for example) Dublin -> London -> Belfast.

What is the distance of the longest route?

"""

import sys
from itertools import permutations


def calc_route(r):
    """ Calcula la distancia total para la ruta dada
    :param r: lista con la ruta de localidades
    :return: distancia entre las localidades de la ruta
    """
    distance = 0
    loc_ant = r[0]
    for loc in range(1, len(r)):
        distance += distances.get((loc_ant, r[loc]), 0)
        loc_ant = r[loc]
    return distance


puzzle_data = sys.stdin.readlines()
locations = []
distances = {}
result_distance = []

for line in puzzle_data:
    x = line.strip().split(" = ")
    origen, destino = x[0].split(" to ")
    if origen not in locations:                 # Añade el origen a la lista de localidades
        locations.append(origen)
    if destino not in locations:                # Añade el destino a la lista de localidades
        locations.append(destino)
    distances[(origen, destino)] = int(x[-1])   # Guarda en dict la distancia origen/destino
    distances[(destino, origen)] = int(x[-1])   # Guarda en dict la distancia destino/origen

routes = permutations(locations)                # Calcula todas las posibles rutas
for route in routes:
    result_distance.append(calc_route(route))   # Calcula la distancia de cada ruta

print("The distance of the shortest route is {0}".format(min(result_distance)))
print("The distance of the longuest route is {0}".format(max(result_distance)))

