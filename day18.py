from math import floor, ceil

filename = 'puzzle_input/day18.txt'
#filename = 'puzzle_input/test_input.txt'

my_input = []
with open(filename) as file:
    for line in file:
        my_input.append(line.strip())


def snum_convert(snum):
    # Converts the string into a list
    # We're using a list so we don't have to worry about 2 digit numbers
    list_snum = []
    for c in snum:
        try:
            list_snum.append(int(c))
        except ValueError:
            list_snum.append(c)
    return list_snum
    

def explode(snum):
    # Keep track of nested depth; if we find a digit and depth > 4, explode
    nested_depth = 0
    prev_num_index = None
    explode = False  # This keeps track of whether we exploded something.
                     # This is used to determine whether we can try to split
                     
    i = 0
    while True:
        c = snum[i]
        if c == ',':
            pass
        elif c == '[':
            nested_depth += 1
        elif c == ']':
            nested_depth -= 1
        else:
            if nested_depth <= 4:
                # Keep track of the index of the last integer we've seen
                prev_num_index = i
            else:
                explode = True
                if prev_num_index is not None:
                    # Add this value to previous integer, if there is one
                    snum[prev_num_index] += c
                
                # Replace this number with zero, then delete stuff
                snum[i] = 0
                del snum[i-1]  # this should be the previous bracket
                del snum[i]  # this should be a comma
                next_num = snum[i]  # this should be 2nd of the exploding pair
                del snum[i]  # delete the number
                del snum[i]  # delete the bracket after the number
                
                # Look for another digit in the rest of the snum
                # If we find it, add the 2nd number of the pair to it
                for n in range(i, len(snum)):
                    if type(snum[n]) == int:
                        snum[n] += next_num
                        break
                # Break if we exploded
                break
        i += 1
        if i >= len(snum):
            # Break if we've reached the end of the snum
            break
    return snum, explode


def split(snum):
    i = 0
    split = False
    while True:  # check each character
        if type(snum[i]) == int and snum[i] > 9:
            split = True
            left = floor(snum[i] / 2)
            right = ceil(snum[i] / 2)
            snum.insert(i + 1, ']')
            snum.insert(i + 1, right)
            snum.insert(i + 1, ',')
            snum.insert(i + 1, left)
            snum[i] = '['
            break
        i += 1
        if i >= len(snum):
            break
    return snum, split
    
    
def reduce(snum):
    # explode() and split() return a bool to indicate whether they actually
    # did anything. We'll use this to decide when we're done
    
    # If we explode something, we should keep exploding until we don't. Then
    # we should always attempt to split. If we split anything, we should always
    # attempt to explode immediately after.
    
    # So we should only split if we didn't explode anything, and we should
    # finish if we don't explode and we don't split.
    keep_exploding = True
    keep_splitting = True
    
    while keep_exploding or keep_splitting:
        if keep_exploding:
            snum, keep_exploding = explode(snum)
            
            # If we've exploded, at some point we must try to split
            if keep_exploding:
                keep_splitting = True
        elif keep_splitting:
            snum, keep_splitting = split(snum)
            
            # If we've split, we must try to explode next time
            if keep_splitting:
                keep_exploding = True
    return snum

                
def add_snums(snum1, snum2):
    snum1 = snum_convert(snum1)
    snum2 = snum_convert(snum2)
    
    snum = ['['] + snum1 + [','] + snum2 + [']']
    snum = reduce(snum)
    
    return snum


def magnitude(snum):
    while len(snum) > 1:
        m = 0
        left = 3
        right = 2
        i = 1
        while True:
            c = snum[i]
            if type(c) == int:
                if snum[i+1] == ',' and type(snum[i+2]) == int:
                    left *= c
                    right *= snum[i+2]
                    try:
                        m = left + right
                    except TypeError:
                        print("error", ''.join([str(c) for c in snum]))
                        return [0]
                    snum[i-1] = m
                    del snum[i:i+4]
                    m = 0
                    left = 3
                    right = 2
            i += 1
            if i >= len(snum):
                break
    return snum
    
    
def sn_display(snum):
    print(''.join([str(c) for c in snum]))

snum_list = []
for this_line in my_input:
    snum_list.append(snum_convert(this_line))
    
first = snum_list[0]
for i in range(1, len(snum_list)):
    second = snum_list[i]
    first = add_snums(first, second)
    
snum = magnitude(first)
print("Part 1:", snum[0])

max_magnitude = 0

for i in range(0, len(snum_list)):
    for j in range(0, len(snum_list)):
        if i != j:
            this_sum = add_snums(snum_list[i], snum_list[j])
            this_sum = magnitude(this_sum)
            if this_sum[0] > max_magnitude:
                max_magnitude = this_sum[0]

print("Part 2:", max_magnitude)

