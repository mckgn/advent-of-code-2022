# Day 8 - Part 2 - Treetop Tree House - Find highest scenic score

x = open('day8/day8_input.txt').read().strip().splitlines()

rows = len(x)
cols = len(x[0])

edges = ((rows * 2) + (cols * 2)) - 4
total = edges
scores = []

for row in range(1, rows - 1):
	for col in range(1, cols - 1):
		tree = x[row][col]
		left = [x[row][col - i] for i in range(1, col + 1)]
		right = [x[row][col + i] for i in range(1, cols - col)]
		up = [x[row - i][col] for i in range(1, row + 1)]
		down = [x[row + i][col] for i in range(1, rows - row)]

		score = 1

		for lst in (left, right, up, down):
			tracker = 0
			for i in range(len(lst)):
				if lst[i] < tree:
					tracker += 1
				elif lst[i] == tree:
					tracker += 1
					break
				else:
					break
			
			score *= tracker
		
		scores.append(score)

print(max(scores))