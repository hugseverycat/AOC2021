filename = "puzzle_input/day9.txt"
#filename = "puzzle_input/test_input.txt"

heightmap = {}

with open(filename) as file:
    for x, line in enumerate(file):
        for y, c in enumerate(line.strip()):
            heightmap[(x, y)] = int(c)

maximum = (x, y)


def get_adjacents(c, m):
    ax = c[0]
    ay = c[1]
    mx = m[0]
    my = m[1]
    
    adjacents = []
    
    if ax < mx:
        adjacents.append((ax + 1, ay))
    if ax > 0:
        adjacents.append((ax - 1, ay))
    if ay < my:
        adjacents.append((ax, ay + 1))
    if ay > 0:
        adjacents.append((ax, ay - 1))
    
    return adjacents

local_minimums = []

for this_loc in heightmap:
    is_local_minimum = True
    for adj in get_adjacents(this_loc, maximum):
        if heightmap[this_loc] >= heightmap[adj]:
            is_local_minimum = False
            break
    if is_local_minimum:
        local_minimums.append(this_loc)

risk = 0

for this_loc in local_minimums:
    risk += 1 + heightmap[this_loc]

print("Part 1:",risk)

visited = []

def find_basin(loc, hm_dict, v_list, m):
    basin_size = 1
    for adj in get_adjacents(loc, m):
        if adj not in v_list:
            v_list.append(adj)
            if hm_dict[adj] != 9:
                basin_size += find_basin(adj, hm_dict, v_list, m)
    return basin_size
      
basin_list = []  
for this_loc in local_minimums:
    visited.append(this_loc)
    basin_list.append(find_basin(this_loc, heightmap, visited, maximum))

basin_list.sort(reverse=True)
print("Part 2:", basin_list[0] * basin_list[1] * basin_list[2])
