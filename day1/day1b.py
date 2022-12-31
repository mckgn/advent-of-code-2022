# Day 1 - Part 2 - Calorie Counting - Top 3 carried calories combined

x = open('day1/day1_input.txt').read().strip().split('\n\n')

e = {}
y = 0
for i in x:
	e['output{0}'.format(y)] = sum(int(b) for b in i.splitlines())
	y += 1

print(sum(sorted(e.values(), reverse=True)[:3]))