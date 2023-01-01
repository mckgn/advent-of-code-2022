# Day 6 - Part 2 - Tuning Trouble - How many characters need to be processed before the first mesage marker is detected

x = open('day6/day6_input.txt').read().strip()

a = 0
g = True
while g == True:
	o = list(x[a:a + 14])
	if len(set(o)) == len(o):
		g = False
		print(a + 14)
	a += 1