from collections import defaultdict

filename = 'puzzle_input/day12.txt'
#filename = 'puzzle_input/test_input.txt'

cave_list = {}


# This is an algorithm I shamelessly stole off stackoverflow and do not understand
def all_simple_paths(caves, start, end, path):
    path = path + [start]
    if start == end:
        return [path]
    paths = []
    for child in caves[start]:
        
        # For part 2, I count how many of each lowercase cave we've visited
        # If we've visited one twice, set twice to True
        twice = False
        for p in path:
            if p.upper() != p:
                temp = path.count(p)
                if temp == 2:
                    twice = True
                    break
                    
        # Switch the 2 ifs below to toggle between part 1 and part 2
        #if child not in path or child.upper() == child:
        if child not in path or child.upper() == child or not twice:
            child_paths = all_simple_paths(caves, child, end, path)
            
            paths.extend(child_paths)
            
    return paths

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

all_paths = all_simple_paths(cave_list, 'start', 'end', [])


# OK so my algorithm above allows us to visit 'start' twice and
# i can't figure out how to fix it
# but i can count how many paths have 'start' in it more than once
# and delete them. so that's what i did.

test_counter = 0
for p in all_paths:
    if p.count('start') > 1:
        test_counter += 1

print("Part 2:", len(all_paths) - test_counter)

    
