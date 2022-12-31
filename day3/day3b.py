# Day 3 - Part 2 - Backpack Reorganization - Sum og the priorities of each group of 3 Elves

x = open('day3/day3_input.txt').read().strip().splitlines()

a = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

start = 0
total = 0

while start < len(x):
	y = x[start:start + 3]
	start += 3

	for char_priority, char in enumerate(a):
		if char in y[0] and char in y[1] and char in y[2]:
			total += char_priority + 1

print(total)