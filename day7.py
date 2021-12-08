from statistics import median, mean
from math import ceil, floor

my_input = []
filename = 'puzzle_input/day7.txt'
#filename = 'puzzle_input/test_input.txt'

with open(filename) as file:
    my_input = [int(i) for i in file.readline().strip().split(',')]
    
median_distance = int(median(my_input))
mean_distance = mean(my_input)

total_fuel_p1 = 0
total_fuel_p2 = 0

p2_1 = 0
p2_2 = 0

for i in my_input:
    total_fuel_p1 += abs(i - median_distance)
    
    d1 = abs(i - ceil(mean_distance))    # because of magic/math, its going
    d2 = abs(i - floor(mean_distance))   # to be one of these
    
    p2_1 += d1 * (d1 + 1) / 2            # formula for sum of numbers 1 to n
    p2_2 += d2 * (d2 + 1) / 2            # is n(n+1)/2
    
    total_fuel_p2 = int(min(p2_1, p2_2))

print("Part 1:", total_fuel_p1)
print("Part 2:", total_fuel_p2)

