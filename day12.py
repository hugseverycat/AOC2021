filename = 'puzzle_input/day12.txt'
filename = 'puzzle_input/test_input.txt'

cave_list = {}

with open(filename) as file:
    for line in file:
        a, b = line.strip().split('-')
        if a not in cave_list:
            cave_list[a] = [b]
        else:
            cave_list[a].append(b)
            
        if b not in cave_list:
            cave_list[b] = [a]
        else:
            cave_list[b].append(a)

for cave in cave_list:
    print(cave, cave_list[cave])
            
