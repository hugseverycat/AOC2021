from collections import deque

my_input = []
filename = 'puzzle_input/day6.txt'
#filename = 'puzzle_input/test_input.txt'

with open(filename) as file:
    my_input = [int(i) for i in file.readline().strip().split(',')]

day_count = 256
fish_count = deque([0 for i in range(0,7)]) # This deque will hold
                                            # fishies with 0-6 days
                                            # til giving birth
age7 = 0
age8 = 0
for i in my_input:
    fish_count[i] += 1

for this_day in range(0, day_count):
    fish_count.rotate(-1)         # The days rotate
    temp_age_8 = fish_count[6]    # New fish are born
    fish_count[6] += age7         # Add age 7 fish to the deque
    age7 = age8                   # Age 8 fish become age 8
    age8 = temp_age_8             # Put new fish into age 8

total_fish = sum(fish_count) + age7 + age8
print(total_fish)

