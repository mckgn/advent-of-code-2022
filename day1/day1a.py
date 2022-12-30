# Day 1 - Part 1 - Calorie Counting - Largest number of carried calories

x = open('day1/day1_input.txt').read().split('\n\n')

e = {}
y = 0
for i in x:
    e['output{0}'.format(y)] = sum(int(b) for b in i.splitlines())
    y += 1

print(max(e.values()))