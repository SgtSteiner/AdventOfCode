def read_input():
    # read input data
    with open("input.txt", 'r') as f:
        return f.readlines()


def feet_paper(boxes):
    # Calc total feet of paper
    total_feet = 0

    for line in boxes:
        box = list(map(int, line.split("x")))
        box.sort()
        area = 2 * box[0] * box[1] + 2 * box[0] * box[2] + 2 * box[1] * box[2]
        smallest_area = box[0] * box[1]
        total_feet += area + smallest_area
    return total_feet


def feet_ribbon(boxes):
    # Calc total feet of ribbon
    total_ribbon = 0

    for line in boxes:
        box = list(map(int, line.split("x")))
        box.sort()
        ribbon = (box[0] + box[0] + box[1] + box[1]) + (box[0] * box[1] * box[2])
        total_ribbon += ribbon
    return total_ribbon


if __name__ == "__main__":
    boxes = [line.rstrip('\n') for line in read_input()]

    print(f"Total square feet = {feet_paper(boxes)}")
    print(f"Total feet of ribbon = {feet_ribbon(boxes)}")

