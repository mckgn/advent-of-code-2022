# Day 5 - Part 2 - Supply Stacks - Find which crate ends up on the top of each stack, with the new model of crane

stacks = ['WLS', 'QNTJ', 'JFHCS', 'BGNWMRT', 'BQHDSLRT', 'LRHFVBJM', 'MJNRWD', 'JDNHFTZB', 'TFBNQLH']

x = open('day5/day5_input.txt').read().strip().splitlines()[10:]

j = []
for i in x:
	j.append([int(i.split(' from ')[0].split('move ')[1]), int(i.split(' from ')[1].split(' to ')[0]), int(i.split(' to ')[1])])

for k in j:
	stacks[k[2] - 1] = stacks[k[1] - 1][:k[0]] + stacks[k[2] - 1]
	stacks[k[1] - 1] = stacks[k[1] - 1][k[0]:]

top_crate = ''
for m in stacks:
	top_crate = top_crate + m[0][0]

print(top_crate)