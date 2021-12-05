part_2 = True

my_input = []
filename = 'puzzle_input/day5.txt'
#filename = 'puzzle_input/test_input.txt'

with open(filename) as file:
    for line in file:
        temp_input = line.strip().split(' -> ')
        pair1 = temp_input[0].split(',')
        pair2 = temp_input[1].split(',')
        pair1 = (int(pair1[0]), int(pair1[1]))
        pair2 = (int(pair2[0]), int(pair2[1]))
        temp_input = [pair1, pair2]
        my_input.append(temp_input)
       
coordinates = {}
    
for this_line in my_input:
    x1 = this_line[0][0]
    x2 = this_line[1][0]
    y1 = this_line[0][1]
    y2 = this_line[1][1]
    min_x = min(x1, x2)
    max_x = max(x1, x2)
    
    min_y = min(y1, y2)
    max_y = max(y1, y2)
    
    try:
        slope = int((y2 - y1) / (x2 - x1))
    except ZeroDivisionError:
        slope = None
    
    if slope is None: # This is a vertical line
        for this_y in range(min_y, max_y + 1):
            if (min_x, this_y) not in coordinates:
                coordinates[(min_x, this_y)] = 0
            else:
                coordinates[(min_x), this_y] += 1
    elif slope == 0: # This is a horizontal line
        for this_x in range(min_x, max_x + 1):
            if (this_x, min_y) not in coordinates:
                coordinates[(this_x, min_y)] = 0
            else:
                coordinates[(this_x, min_y)] += 1
    elif abs(slope) == 1: # This is a diagonal line
        if not part_2:
            pass
        else:
            if min_x == x1:
                start_y = y1
            else:
                start_y = y2
            for this_x in range(min_x, max_x + 1):
                
                if (this_x, start_y) not in coordinates:
                    coordinates[(this_x, start_y)] = 0
                else:
                    coordinates[(this_x, start_y)] += 1
                start_y += slope

    else:
        print("Unexpected slope found for line", this_line)
        print("Slope is", slope)

intersection_count = 0
for this_c in coordinates:
    if coordinates[this_c] > 0:
        intersection_count += 1

print(intersection_count)
