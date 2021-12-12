from collections import defaultdict

filename = 'puzzle_input/day12.txt'
filename = 'puzzle_input/test_input.txt'

cave_list = {}

def all_simple_paths(caves, start, end, path):
    path = path + [start]
    if start == end:
        return [path]
    paths = []
    for child in caves[start]:
        twice = False
        visited = list(map(lambda letter: {letter: path.count(letter)}, set(path)))
        print(visited)
        print(len(visited))
        '''for v in visited:
            if visited[v] > 1 and v.upper() != v:
                twice = True'''
        #if child not in path or child.upper() == child:
        if child != 'start' and (child not in path or child.upper() == child):
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

'''for cave in cave_list:
    print(cave, cave_list[cave])'''

visits = defaultdict(int)
all_paths = all_simple_paths(cave_list, 'start', 'end', [])
'''for this_path in all_paths:
    print(this_path)'''

print(len(all_paths))
#print(visits)
    
