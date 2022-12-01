"""_summary_: https://adventofcode.com/2022/day/1

"""
    
def read_input():
    with open("input.txt", 'r') as f:
        return f.readlines()

def calories_top_elves(data, top):
    elves = {}
    n_elve = 1
    for calorie in data:
        if calorie:
            elves[n_elve] = elves.get(n_elve, 0) + int(calorie)
        else:
            n_elve += 1
    return sum(sorted(elves.values(), reverse=True)[:top])

if __name__ == "__main__":
    data = [item.rstrip('\n') for item in read_input()]
    print(f"Calories of the Elf carrying the most calories: {calories_top_elves(data, 1)}")    
    print(f"Calories of the top three Elves carrying the most Calories: {calories_top_elves(data, 3)}")
    