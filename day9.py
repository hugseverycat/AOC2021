filename = "puzzle_input/day9.txt"
#filename = "puzzle_input/test_input.txt"

heightmap = {}

with open(filename) as file:
    for x, line in enumerate(file):
        for y, c in enumerate(line.strip()):
            heightmap[(x, y)] = int(c)

maximum = (x, y)


def get_adjacents(c, m):
    # Function to get all valid coordinates adjacent to c = (x,y)
    # m = (max_x, max_y)
    
    # Pulling them out into variables because i hate typing brackets
    ax = c[0]
    ay = c[1]
    mx = m[0]
    my = m[1]
    
    adjacents = []
    
    # Check whether the adjacent coords are valid and if so, add to list
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

# Here we loop through each location, find its adjacents, then see if 
# there are any lower.
for this_loc in heightmap:
    is_local_minimum = True
    for adj in get_adjacents(this_loc, maximum):
        if heightmap[this_loc] >= heightmap[adj]:
            # If we find a lower adjacent coord, this isn't a local
            # minimum and we can stop checking.
            is_local_minimum = False
            break
    if is_local_minimum:
        local_minimums.append(this_loc)

risk = 0

for this_loc in local_minimums:
    risk += 1 + heightmap[this_loc]

print("Part 1:",risk)


'''Part 2 starts here'''

# A list to keep track of the locations we've already checked
# since no location can be in 2 or more basins.
visited = []

def find_basin(loc, hm_dict, v_list, m):
    # A recursive function to find the size of a basin.
    # This function will first check find the adjacents of the location.
    # For each adjacent, it will check whether it has been visited already.
    # If not, it will check whether the location is 9.
    # If not, then it will call itself recursively and add that value
    # to the basin size.
    
    # We start with basin size 1 because this location we're checking
    # has already been determined to be part of the basin, because it is
    # either the local minimum or we've already found it's not a 9.
    basin_size = 1
    
    for adj in get_adjacents(loc, m):
        if adj not in v_list:
            # Add this adjacent location to the visited list
            v_list.append(adj)
            if hm_dict[adj] != 9:
                # If it's not a 9, call the function again!
                basin_size += find_basin(adj, hm_dict, v_list, m)
    return basin_size
      
basin_list = []  
for this_loc in local_minimums:
    visited.append(this_loc)    # Add this local min to the visited list
    basin_list.append(find_basin(this_loc, heightmap, visited, maximum))

basin_list.sort(reverse=True)
print("Part 2:", basin_list[0] * basin_list[1] * basin_list[2])

