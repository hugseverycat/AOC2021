from statistics import median
from statistics import mean

my_input = []
filename = 'puzzle_input/day7.txt'
#filename = 'puzzle_input/test_input.txt'

with open(filename) as file:
    my_input = [int(i) for i in file.readline().strip().split(',')]
    
median_distance = int(median(my_input))
mean_distance = int(mean(my_input))

total_fuel_p1 = 0
total_fuel_p2 = 0
p2_candidates = [0, 0, 0]

for i in my_input:
    total_fuel_p1 += abs(i - median_distance)
    
    # The optimal distance should be within 1 of the calculated mean
    # So we will get all 3 then find the minimum
    p2_candidates[0] += sum([n for n in range(1, abs(i - mean_distance) + 1)])
    p2_candidates[1] += sum([n for n in range(1, abs(i - mean_distance + 1) + 1)])
    p2_candidates[2] += sum([n for n in range(1, abs(i - mean_distance - 1) + 1)])
    total_fuel_p2 = min(p2_candidates)

print("Part 1:", total_fuel_p1)
print("Part 2:", total_fuel_p2)
