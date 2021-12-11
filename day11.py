filename = 'puzzle_input/day11.txt'
#filename = 'puzzle_input/test_input.txt'

octopuses = {}

with open(filename) as file:
    for x, line in enumerate(file):
        for y, c in enumerate(line.strip()):
            octopuses[(x, y)] = int(c)


def get_adjacents(coord):
    # A function to get 
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
    # A recursive function to flash an octopus and flash any
    # neighbors as well
    f_list.append(coord)    # f_list keeps track of which have flashed this step
    octo_dict[coord] = 0    # set the flashed octopus to zero
    octo_adjacents = get_adjacents(coord)
    for this_adj in octo_adjacents:
        if this_adj not in f_list:
            octo_dict[this_adj] += 1
        if octo_dict[this_adj] == 10:    # if an adjacent octopus hits 10, flash it
            flash(this_adj, octo_dict, f_list)

flash_count = 0
step_count = 0

while True:
    flash_queue = []    # list of octopuses to flash after initial increase
    flash_list = []     # list of octopuses that have flashed this step
    
    # increase each octopus by 1
    for this_octopus in octopuses:
        octopuses[this_octopus] += 1
        if octopuses[this_octopus] == 10:
            flash_queue.append(this_octopus)
    
    # flash!!
    for this_octopus in flash_queue:
        flash(this_octopus, octopuses, flash_list)
    flash_count += len(flash_list)
    step_count += 1
    
    if step_count == 100:
        print("Part 1:", flash_count)
    
    # if all 100 octopuses have flashed, part 2 is complete
    if len(flash_list) == 100:
        print("Part 2:", step_count)
        break

