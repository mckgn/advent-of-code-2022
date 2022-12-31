# Day 1 - Part 1 - Calorie Counting - Largest number of carried calories

x = open('day1/day1_input.txt').read().strip().split('\n\n')

y = {}
z = 0
for i in x:
	y['output{0}'.format(z)] = sum(int(b) for b in i.splitlines())
	z += 1

print(max(y.values()))