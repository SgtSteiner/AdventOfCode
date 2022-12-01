"""
--- Day 10: Elves Look, Elves Say ---
http://adventofcode.com/2015/day/10

Today, the Elves are playing a game called look-and-say. They take turns making sequences
by reading aloud the previous sequence and using that reading as the next sequence.
For example, 211 is read as "one two, two ones", which becomes 1221 (1 2, 2 1s).

Look-and-say sequences are generated iteratively, using the previous value as input for the next step.
For each step, take the previous value, and replace each run of digits (like 111)
with the number of digits (3) followed by the digit itself (1).

For example:

. 1 becomes 11 (1 copy of digit 1).
. 11 becomes 21 (2 copies of digit 1).
. 21 becomes 1211 (one 2 followed by one 1).
. 1211 becomes 111221 (one 1, one 2, and two 1s).
. 111221 becomes 312211 (three 1s, two 2s, and one 1).

Starting with the digits in your puzzle input, apply this process 40 times. What is the length of the result?

--- Part Two ---

Neat, right? You might also enjoy hearing John Conway talking about this sequence
(that's Conway of Conway's Game of Life fame).

Now, starting again with the digits in your puzzle input, apply this process 50 times.
What is the length of the new result?

Your puzzle input is still 1113222113.

"""

sequence = input().strip()
print(sequence)

for i in range(50):
    conta_num = 0
    new_sequence = ""
    num_ant = sequence[0]
    for num_cur in sequence:
        if num_cur == num_ant:
            conta_num += 1
        else:
            new_sequence += str(conta_num) + num_ant
            num_ant = num_cur
            conta_num = 1
    new_sequence += str(conta_num) + num_cur
    sequence = new_sequence

print("The length of the sequence: {0}".format(len(sequence)))
