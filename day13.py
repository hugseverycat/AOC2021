filename = 'puzzle_input/day13.txt'
#filename = 'puzzle_input/test_input.txt'

coords = set()    # Storing as a set so we don't have to worry about duplicates
folds = []
raw_input = []
max_x = 0
max_y = 0

with open(filename) as file:
    for line in file:
        # When we hit the blank line, take all the input we've found
        # so far and process it into the coords set
        if line.strip() == '':
            for this_input in raw_input:
                x, y = this_input.split(',')
                x, y = int(x), int(y)
                coords.add((x, y))
            # Clear the raw_input list; now we will store folds in it
            raw_input = []
        else:
            raw_input.append(line.strip())

# Process the folds from the raw_input list into the folds list
for this_input in raw_input:
    temp = this_input.split('=')
    axis = temp[0][-1]
    value = int(temp[1])
    folds.append((axis, value))


def do_fold(coord_set, fold):
    f_axis, f_value = fold
    new_coord_set = set()
    
    for this_coord in coord_set:
        cx, cy = this_coord
        if f_axis == 'x':
            # If cx is bigger than the fold, its x value will change
            # The formula for how it will change is 2 * fold - cx
            
            # If cx is smaller, then it wont change, just add to new set
            if cx > f_value:
                new_coord_set.add((2 * f_value - cx, cy))
            else:
                new_coord_set.add((cx, cy))
        else:  # f_axis == 'y'
            # Same as above, but for cy now.
            if cy > f_value:
                new_coord_set.add((cx, 2 * f_value - cy))
            else:
                new_coord_set.add((cx, cy))
    return new_coord_set

for this_fold in folds:
    coords = do_fold(coords, this_fold)

# Find the max x and y for printing purposes
for this_c in coords:
    tx, ty = this_c
    if tx > max_x:
        max_x = tx
    if ty > max_y:
        max_y = ty

# Print them out
for y in range(0, max_y + 1):
    line = ''
    for x in range(0, max_x + 1):
        if (x, y) in coords:
            line += '#'
        else:
            line += ' '
    print(line)

