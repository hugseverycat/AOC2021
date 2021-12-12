from collections import deque
filename = 'puzzle_input/day12.txt'
filename = 'puzzle_input/test_input.txt'

caves = {}

with open(filename) as file:
    for line in file:
        a, b = line.strip().split('-')
        if a not in caves:
            caves[a] = deque([b])
        else:
            if b not in caves[a]:
                caves[a].append(b)
        if b not in caves:
            caves[b] = deque([a])
        else:
            if a not in caves[b]:
                caves[b].append(a)

for c in caves:
    print(c, caves[c])

caves['b'].rotate(2)
print(caves['b'])
    
def get_path(cave_list):
    current_cave = 'start'
    current_path = [current_cave]
    dead_ends = []
    iter_count = 0
    
    while current_cave != 'end':
        iter_count = 0
        for next_cave in cave_list[current_cave]:
            if next_cave not in dead_ends:
                if next_cave not in current_path or next_cave.upper() == next_cave:
                    current_path.append(next_cave)
                    current_cave = next_cave
                    break
                iter_count += 1
                if iter_count == len(cave_list[current_cave]):
                    print("dead end found at", current_cave)
                    dead_ends.append(current_cave)
    print(iter_count)
    return current_path

print()
print(get_path(caves))

