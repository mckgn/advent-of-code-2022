# Day 4 - Part 1 - Camp Cleanup - Number of pairs that one range full contains the other

x = open('day4/day4_input.txt').read().strip().splitlines()

counter = 0

for y in range(len(x)):
	n = list(range(int((x[y].split(',')[0].split('-')[0])), int((x[y].split(',')[0].split('-')[1])) + 1))
	m = list(range(int((x[y].split(',')[1].split('-')[0])), int((x[y].split(',')[1].split('-')[1])) + 1))

	if set(n).issubset(m) or set(m).issubset(n):
		counter += 1

print(counter)