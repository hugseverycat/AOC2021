filename = 'day1.txt'
my_input = []
increase_count_part_1 = 0
increase_count_part_2 = 0

with open(filename) as file:
	for line in file:
		my_input.append(int(line.strip()))

measure_count = len(my_input)
for i in range (1, measure_count):
	if my_input[i-1] < my_input[i]:
		increase_count_part_1 += 1
		
for i in range(3, measure_count):
	if (my_input[i-1] + my_input[i-2] + my_input[i-3]) < (my_input[i] + my_input[i-1] + my_input[i-2]):
		increase_count_part_2 += 1

print("Part 1: " + str(increase_count_part_1))
print("Part 2: " + str(increase_count_part_2))

