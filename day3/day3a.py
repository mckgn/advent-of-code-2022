# Day 3 - Part 1 - Backpack Reorganization - Sum of the priorities of items existing in both compartments

x = open('day3/day3_input.txt').read().strip().splitlines()

a = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

total = 0

for p in x:
	lh = p[:len(p) // 2]
	rh = p[len(p) // 2:]

	for char_priority, char in enumerate(a):
		if char in lh and char in rh:
			total += char_priority + 1

print(total)