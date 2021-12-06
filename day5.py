part_2 = True

my_input = []
filename = 'puzzle_input/day5.txt'
#filename = 'puzzle_input/test_input.txt'

with open(filename) as file:
    # Process the input so each item in my_input is [(x1, y1), (x2, y2)]
    for line in file:
        temp_input = line.strip().split(' -> ')
        pair1 = temp_input[0].split(',')
        pair2 = temp_input[1].split(',')
        pair1 = (int(pair1[0]), int(pair1[1]))
        pair2 = (int(pair2[0]), int(pair2[1]))
        temp_input = [pair1, pair2]
        my_input.append(temp_input)
  
# Each key will be (x, y) = n where n is the number of intersections
coordinates = {}
    
for this_line in my_input:
    # Getting all our coords into variables for ease of use later
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
        slope = None # Divide by zero means vertical line
    
    if slope is None: # This is a vertical line
        for this_y in range(min_y, max_y + 1):
            # For vertical lines, x is constant, so I'm just using max_x
            # Record the coordinates for each y from min to max
            if (min_x, this_y) not in coordinates:
                # If this coordinate hasn't been visited yet, add it
                coordinates[(min_x, this_y)] = 0
            else:
                # If it has, increase its number of intersections
                coordinates[(min_x), this_y] += 1
                
    elif slope == 0: # This is a horizontal line
        for this_x in range(min_x, max_x + 1):
            # For horizontal lines, y is constant
            if (this_x, min_y) not in coordinates:
                coordinates[(this_x, min_y)] = 0
            else:
                coordinates[(this_x, min_y)] += 1
                
    elif abs(slope) == 1: # This is a diagonal line
        if not part_2:
            pass
        else:
            # Start with min_x and its corresponding y
            if min_x == x1:
                start_y = y1
            else:
                start_y = y2
            for this_x in range(min_x, max_x + 1):
                # Since we're starting with the minimum x, we can increase it by 1
                # until we reach the maximum x.
                
                # We will increase y by the slope (either 1 or -1)
                if (this_x, start_y) not in coordinates:
                    coordinates[(this_x, start_y)] = 0
                else:
                    coordinates[(this_x, start_y)] += 1
                start_y += slope

    else:
        print("Unexpected slope found for line", this_line)
        print("Slope is", slope)

intersection_count = 0

# Count how many coordinates have any intersections
for this_c in coordinates:
    if coordinates[this_c] > 0:
        intersection_count += 1

print(intersection_count)
