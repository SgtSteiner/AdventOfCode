def read_input():
    with open("input.txt", 'r') as f:
        return f.readlines()


def read_bag_rule(s):
    n = 0
    t = c = thing = ""
    if s.strip().split()[0].isnumeric():
        n, t, c, thing = s.strip().split()
    return int(n), t + " " + c


def bag_count(bags):
    colors = []
    if dict_bag.get(bags):
        colors = dict_bag[bags]
        for element in dict_bag[bags]:
            colors += bag_count(element)
    print(bags)
    return colors


# def bag_count(bags):
#     colors = 0
#     if dict_bag.get(bags, None):
#         color = len(set(dict_bag[bags]))
#         x = dict_bag[bags]
#         for element in dict_bag[bags]:
#             colors += bag_count(element)
#     return colors


if __name__ == "__main__":
    rules = read_input()

    dict_bag = {}
    for rule in rules:
        bag_outside, bags_inside = rule.split("contain")
        for bags in bags_inside.split(","):
            number, colour = read_bag_rule(bags)
            if number > 0:
                colour_outside = bag_outside.strip().split()
                colour_outside = " ".join(colour_outside[:2])
                dict_bag[colour] = dict_bag.get(colour, []) + [colour_outside]

    print(bag_count("shiny gold"))
    print(len(set(bag_count("shiny gold"))))
