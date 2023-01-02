# Day 2 - Part 2 - Rock, Paper, Scissors - Scored based on corrected strategy guide

x = open('day2/day2_input.txt').read().strip().splitlines()

outcomes = {'A X' : 3, 'A Y' : 4, 'A Z' : 8, 'B X' : 1, 'B Y' : 5, 'B Z' : 9, 'C X' : 2, 'C Y' : 6, 'C Z' : 7}

total_score = 0

for y in x:
	total_score = total_score + outcomes[y]

print(total_score)