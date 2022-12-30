# Day 1 - Part 1 - Calorie Counting

d1_file = 'day1_input.txt'

with open(d1_file) as d1_f:
    d1_contents = d1_f.read()

e = {}
for y in range(len(d1_contents.split('\n\n'))):
    e["output{0}".format(y)] = sum((int(b) for b in d1_contents.split('\n\n')[y].replace('\n', ',').strip(',').split(',')))

max(e.values())