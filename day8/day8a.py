# Day 8 - Part 1 - Treetop Tree House - Find number of trees visible outside the grid

x = open('day8/day8_input.txt').read().strip().splitlines()

rows = len(x)
cols = len(x[0])

edges = ((rows * 2) + (cols * 2)) - 4
total = edges

for row in range(1, rows - 1):
	for col in range(1, cols - 1):
		tree = x[row][col]
		left = [x[row][col - i] for i in range(1, col + 1)]
		right = [x[row][col + i] for i in range(1, cols - col)]
		up = [x[row - i][col] for i in range(1, row + 1)]
		down = [x[row + i][col] for i in range(1, rows - row)]

		if max(left) < tree or max(right) < tree or max(up) < tree or max(down) < tree:
			total += 1

print(total)