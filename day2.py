filename = 'puzzle_input/day2.txt'
my_input = []
x_pos = 0
y_pos = 0

with open(filename) as file:
    for line in file:
        this_input = line.split()
        this_input[1] = int(this_input[1])

        if this_input[0] == 'forward':
            x_pos += this_input[1]
        elif this_input[0] == 'up':
            y_pos -= this_input[1]
        elif this_input[0] == 'down':
            y_pos += this_input[1]
        else:
            print("unexpected direction: ", this_input[0])
            break

        my_input.append(this_input)

print("Part 1: ", y_pos * x_pos)

x_pos = 0
y_pos = 0
aim = 0

for this_inst in my_input:

    if this_inst[0] == 'forward':
        x_pos += this_inst[1]
        y_pos += aim * this_inst[1]
    elif this_inst[0] == 'up':
        aim -= this_inst[1]
    elif this_inst[0] == 'down':
        aim += this_inst[1]
    else:
        print("unexpected direction: ", this_inst[0])
        break


print("Part 2: ", y_pos * x_pos)

