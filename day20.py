filename = 'puzzle_input/day20.txt'
#filename = 'puzzle_input/test_input.txt'

image = {}

with open(filename) as file:
    img_algo = file.readline().strip()
    _ = file.readline().strip()
    
    for y, line in enumerate(file):
        this_line = line.strip()
        for x, c in enumerate(this_line):
            image[(x, y)] = c
            

def get_neighbors(coord):
    cx, cy = coord

    return[(cx-1, cy-1), (cx, cy-1), (cx+1, cy-1), (cx-1, cy), (cx, cy),
           (cx+1, cy), (cx-1, cy+1), (cx, cy+1), (cx+1, cy+1)]
    
    
def display_image(partial_image):
    # This was used for debugging but not in the actual solution
    new_line = ' '
    for x in range(-10, 10):
        new_line += str(abs(x))[0]
    print(new_line)
    for y in range(-8, 10):
        new_line = str(abs(y))[0]
        for x in range(-5, 10):
            if (x, y) in image:
                new_line += image[(x, y)]
            else:
                new_line += ' '
        print(new_line)
    print()


def to_decimal(img_str):
    bin_str = ''
    for c in img_str:
        if c == '.':
            bin_str += '0'
        else:
            bin_str += '1'
    return int(bin_str, 2)


def expand(partial_image):
    # Out of frustration, I just expanded it hugely instead of smartly
    min_x = -100
    max_x = 200
    min_y = -100
    max_y = 200
    
    for ty in range(min_y, max_y):
        for tx in range(min_x, max_x):
            if (tx, ty) not in partial_image:
                partial_image[(tx, ty)] = '.'

    return partial_image


def enhance(partial_image, algo, enh_count):
    # Determine whether new pixels at the edge are . or #
    if enh_count % 2 == 0:
        d = '.'
    else:
        d = '#'
    
    # Create new dictionary to store the enhanced image
    enh_image = {}
    for location in partial_image:
        neighbors = get_neighbors(location)
        decode = ''
        
        # Create the decode string. For pixels on the edge, use d
        for n in neighbors:
            if n in partial_image:
                decode += partial_image[n]
            else:
                decode += d
        
        # Get the decimal index for the image algorithm
        decode = to_decimal(decode)
        
        # Update the pixel
        enh_image[location] = algo[decode]
    return enh_image

image = expand(image)
enh_count = 50

for i in range(enh_count):
    print("enhancing:", i)
    image = enhance(image, img_algo, i)
    print()

pixel_count = 0
for loc in image:
    if image[loc] == '#':
        pixel_count += 1

print(pixel_count)

