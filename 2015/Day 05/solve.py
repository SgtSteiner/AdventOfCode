BAD_CHAINS = ["ab", "cd", "pq", "xy"]
VOWELS = "aeiou"


def read_input():
    # read input data
    with open("input.txt", 'r') as f:
        return f.readlines()


def contain_three_vowels(s):
    conta = 0
    for char in s:
        if char.lower() in VOWELS:
            conta += 1
    return conta >= 3


def contain_bad_chain(s):
    for chain in BAD_CHAINS:
        if chain in s.lower():
            return True
    return False


def letter_appears_twice(s):
    previous_letter = ""
    for letter in s:
        if letter == previous_letter:
            return True
        previous_letter = letter


def pair_appears_twice(s):
    pair = [" ", " "]
    for char in s:
        pair.pop(0)
        pair.append(char)
        if s.count("".join(pair)) >= 2:
            return True
    return False


def one_letter_between_them(s):
    trio = [" ", " ", " "]
    for char in s:
        trio.pop(0)
        trio.append(char)
        if trio[0] == trio[2]:
            return True
    return False


def count_nice_one(words):
    conta = 0
    for word in words:
        if contain_three_vowels(word) and letter_appears_twice(word) and not contain_bad_chain(word):
            conta += 1
    return conta


def count_nice_two(words):
    conta = 0
    for word in words:
        if pair_appears_twice(word) and one_letter_between_them(word):
            conta += 1
    return conta


if __name__ == "__main__":
    words = [word.rstrip('\n') for word in read_input()]

    print(f"Parte One - String nice are {count_nice_one(words)}")
    print(f"Parte Two - String nice are {count_nice_two(words)}")
