filename = 'puzzle_input/day11.txt'
#filename = 'puzzle_input/test_input.txt'

octopuses = {}

with open(filename) as file:
    for x, line in enumerate(file):
        for y, c in enumerate(line.strip()):
            octopuses[(x, y)] = int(c)


def get_adjacents(coord):
    ax, ay = coord[0], coord[1]
    adj_list = []
    for i in range(-1, 2):
        for j in range(-1, 2):
            nx = ax + i
            ny = ay + j
            if nx in range(0, 10) and ny in range(0, 10) and not (i == j == 0):
                adj_list.append((nx, ny))
    return adj_list


def flash(coord, octo_dict, f_list):
    f_list.append(coord)
    octo_dict[coord] = 0
    octo_adjacents = get_adjacents(coord)
    for this_adj in octo_adjacents:
        if this_adj not in f_list:
            octo_dict[this_adj] += 1
        if octo_dict[this_adj] == 10:
            flash(this_adj, octo_dict, f_list)

flash_count = 0
step_count = 0

while True:
    flash_queue = []
    flash_list = []
    for this_octopus in octopuses:
        octopuses[this_octopus] += 1
        if octopuses[this_octopus] == 10:
            flash_queue.append(this_octopus)
    
    for this_octopus in flash_queue:
        flash(this_octopus, octopuses, flash_list)
    flash_count += len(flash_list)
    step_count += 1
    if step_count == 100:
        print("Part 1:", flash_count)
    if len(flash_list) == 100:
        print("Part 2:", step_count)
        break

