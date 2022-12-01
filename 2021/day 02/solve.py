def read_input():
    with open("input.txt", 'r') as f:
        return f.readlines()


def part_one(data):
    horizontal_pos_ = 0
    depth_ = 0

    for movement, value in data:
        if movement == "forward":
            horizontal_pos_ += int(value)
        elif movement == "down":
            depth_ += int(value)
        elif movement == "up":
            depth_ -= int(value)
            if depth_ < 0:
                depth_ = 0
    return horizontal_pos_, depth_


def part_two(data):
    horizontal_pos_ = 0
    depth_ = 0
    aim = 0

    for movement, value in data:
        if movement == "forward":
            horizontal_pos_ += int(value)
            if aim > 0:
                depth_ += (aim * int(value))
        elif movement == "down":
            aim += int(value)
        elif movement == "up":
            aim -= int(value)
            if aim < 0:
                aim = 0
    return horizontal_pos_, depth_


if __name__ == "__main__":
    data = [item.rstrip('\n').split() for item in read_input()]

    horizontal_pos, depth = part_one(data)
    print(f"Part one: {horizontal_pos * depth}")

    horizontal_pos, depth = part_two(data)
    print(f"Part two: {horizontal_pos * depth}")
