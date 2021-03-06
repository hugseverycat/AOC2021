from collections import deque

my_input = []
filename = 'puzzle_input/day6.txt'
# filename = 'puzzle_input/test_input.txt'

with open(filename) as file:
    my_input = [int(i) for i in file.readline().strip().split(',')]

day_count = 256
fish_count = deque([0 for i in range(0,9)])    # all fishies are stored
                                               # in a deque by how many
                                               # days til they give birth

for i in my_input:
    fish_count[i] += 1

for this_day in range(0, day_count):
    fish_count.rotate(-1)             # Days til giving birth rotate
    
    fish_count[6] += fish_count[8]    # So the count at 0 has been rotated
                                      # to 8. This indicates the fish just born.
                                      # But the parents of these fish need
                                      # to be added to 6. I promise it makes sense
                                      

total_fish = sum(fish_count)
print(total_fish)

