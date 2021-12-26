filename = 'puzzle_input/day25.txt'
#filename = 'puzzle_input/test_input.txt'

east_herd = set()
south_herd = set()
WIDTH = 0
HEIGHT = 0

with open(filename) as file:
    for y, line in enumerate(file):
        HEIGHT += 1
        WIDTH = len(line.strip())
        for x, c in enumerate(line.strip()):
            if c == '>':
                east_herd.add((x, y))
            elif c == 'v':
                south_herd.add((x, y))

def get_next(cuc, eh, sh):
    # A function to get the next position of a sea cucumber, if it moves
    cx, cy = cuc
    
    # Modulos to move sea cucumbers to the beginning
    if cuc in eh:
        cx = (cx + 1) % WIDTH
    elif cuc in sh:
        cy = (cy + 1) % HEIGHT
    else:
        print("There is no cucumber at", cx, cy)
    
    return (cx, cy)
    
def do_step(eh, sh):
    # A function to do an entire step of movement
    moved = None
    
    # New sets to hold the east-going and south-going herds
    new_east = set()
    new_south = set()
    moved = 0

    for cucumber in eh:
        # Check whether any other sea cucumbers are in the position this cucumber
        # wants to move to
        x, y = get_next(cucumber, eh, sh)
        
        # If there is a sea cucumber, this one doesn't move. add its current position
        # to the new set.
        if (x, y) in eh or (x, y) in sh:
            new_east.add(cucumber)
        else:
            new_east.add((x, y))
            moved += 1

    for cucumber in sh:
        # Check the south-going sea cucumbers
        x, y = get_next(cucumber, eh, sh)
        
        # Looking at the new_east set as those cuces have already moved
        if (x, y) in new_east or (x, y) in sh:
            new_south.add(cucumber)
            pass
        else:
            new_south.add((x, y))
            moved += 1
    
    eh = new_east
    sh = new_south
    
    return new_east, new_south, moved

moved = None
n = 0
while moved != 0:
    east_herd, south_herd, moved = do_step(east_herd, south_herd)
    n += 1

print(n)

