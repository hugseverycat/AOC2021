data = open('puzzle_input/day1.txt')

controls = []
for i in data:
	controls.append(int(i))


controls.sort()
print(controls)
