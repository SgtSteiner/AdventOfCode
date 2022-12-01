def read_input():
    with open("input.txt", 'r') as f:
        return f.readlines()


def part_one(data):
    gamma_ = ""
    epsilon_ = ""

    for index in range(len(data[0])):
        sum_bit = sum(int(item[index]) for item in data)
        if sum_bit > len(data)/2:   # Calculamos el bit más común
            gamma_ += "1"
            epsilon_ += "0"
        else:
            gamma_ += "0"
            epsilon_ += "1"

    return int(gamma_, 2), int(epsilon_, 2)


def part_two(data, parameter):
    current_data = data
    for index in range(len(current_data[0])):
        items_bit_1 = [item for item in current_data if item[index] == "1"]
        items_bit_0 = [item for item in current_data if item[index] == "0"]
        if parameter == "oxygen":
            if len(items_bit_1) >= len(current_data)/2:
                current_data = items_bit_1
            else:
                current_data = items_bit_0
        elif parameter == "co2":
            if len(items_bit_0) <= len(current_data) / 2:
                current_data = items_bit_0
            else:
                current_data = items_bit_1
        if len(current_data) == 1:
            break

    print(current_data[0])
    return int("".join(current_data[0]), 2)


if __name__ == "__main__":
    data = [list(item.rstrip('\n')) for item in read_input()]

    gamma, epsilon = part_one(data)
    print(f"Part one: {gamma * epsilon}")

    oxygen = part_two(data, "oxygen")
    co2 = part_two(data, "co2")
    print(f"Part two: {oxygen * co2}")



