def read_input():
    with open("input.txt", 'r') as f:
        return f.readlines()


if __name__ == "__main__":
    data = [int(item.rstrip('\n')) for item in read_input()]

    print(sum([data[i] > data[i-1] for i in range(1, len(data))]))

    three_measurement = [data[i] + data[i+1] + data[i+2] for i in range(len(data)-2)]
    print(sum([three_measurement[i] > three_measurement[i - 1] for i in range(1, len(three_measurement))]))

