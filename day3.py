filename = 'puzzle_input/day3.txt'
my_input = []

with open(filename) as file:
    for line in file:
        my_input.append(line.strip())


def get_most_common(gmc_list, gmc_index):
    # gmc_list is the input list
    # gmc_index is which position we are looking at
    
    l_len = len(gmc_list)
    gmc_counter = 0
    
    for this_l in gmc_list:
        gmc_counter += int(this_l[gmc_index])
    if gmc_counter >= l_len / 2:
        return '1'
    else:
        return '0'
        

input_length = len(my_input)
num_length = len(my_input[0])
gamma = ""
epsilon = ""

for c in range(num_length):
    most_common = get_most_common(my_input, c)
    if most_common == '1':
        gamma += '1'
        epsilon += '0'
    else:
        epsilon += '1'
        gamma += '0'
    
print("Part 1:", int(gamma, 2) * int(epsilon, 2))

o2_list = []
co2_list = []
first_mc = get_most_common(my_input, 0)

# First, we will split input_list into 2 separate lists for o2 and co2
for c in range(input_length):
    if my_input[c][0] == first_mc:
        o2_list.append(my_input[c])
    else:
        co2_list.append(my_input[c])


def reduce_list(this_list, switch):
    '''
    a function to reduce a given list to 1 item
    this_list is the list we are reducing
    switch is 0 or 1, to determine whether we want the most common or
    least common
    '''
    
    c = 1    # setting the index to 1 because we already checked index 0
    list_len = len(this_list)
    
    # this will go through and reduce the list index by index until only
    # 1 remains
    while list_len > 1:
        mc = get_most_common(this_list, c)
        
        # if we're looking for least common instead of most common, then
        # flip mc
        if switch == 0:
            if mc == '0':
                mc = '1'
            else:
                mc = '0'
        i = 0
        
        # delete every item that doesnt have the most common bit in pos c
        while i < list_len:
            if this_list[i][c] == mc:
                i += 1    # only increment the index if not deleting
            else:
                del this_list[i]
                list_len -= 1
        c += 1
        
    return this_list[0]

print("Part 2:", int(reduce_list(o2_list, 1), 2) *
      int(reduce_list(co2_list, 0), 2))

