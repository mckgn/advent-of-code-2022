# Day 2 - Part 1 - Rock, Paper, Scissors - Total score based on strategy guide

x = open('day2/day2_input.txt').read().strip().splitlines()

outcomes = {'A X' : 4, 'A Y' : 8, 'A Z' : 3, 'B X' : 1, 'B Y' : 5, 'B Z' : 9, 'C X' : 7, 'C Y' : 2, 'C Z' : 6}

total_score = 0

for y in x:
	total_score = total_score + outcomes[y]

print(total_score)