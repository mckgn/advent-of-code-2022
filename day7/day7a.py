# Day 7 - Part 1 - No Space Left On Device - Sum of total size of all directories less than 100000

x = open('day7/day7_input.txt').read().strip().splitlines()

path = '/home'
dirs = {'/home' : 0}

for y in x:
	if y[0] == '$':
		if y[2:4] == 'ls':
			pass
		elif y[2:4] == 'cd':
			if y[5:6] == '/':
				path = '/home'
			elif y[5:7] == '..':
				path = path[:path.rfind('/')]
			else:
				dir_name = y[5:]
				path = path + '/' + dir_name
				dirs.update({path : 0})
	elif y[0:3] == 'dir':
		pass
	else:
		size = int(y[:y.find(' ')])
		dir = path
		for i in range(path.count('/')):
			dirs[dir] += size
			dir = dir[:dir.rfind('/')]

total = 0

for path in dirs:
	if dirs[path] <= 100000:
		total += dirs[path]

print(total)