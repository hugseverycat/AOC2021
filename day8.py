filename = "puzzle_input/day8.txt"
#filename = "puzzle_input/test_input.txt"

my_input = []

with open(filename) as file:
    for line in file:
        temp = [l.split() for l in line.strip().split(' | ')]
        
        # Sorting each string alphabetically
        temp[0] = [''.join(sorted(ss)) for ss in temp[0]]
        temp[1] = [''.join(sorted(ss)) for ss in temp[1]]
        my_input.append(temp)
        
# Do part 1
counter = 0
for this_input in my_input:
    for this_output in this_input[1]:
        if len(this_output) in (2, 3, 4, 7):
            
            counter += 1

print("Part 1:", counter)

# Do part 2
def in_string(sub_s, main_s):
    # Determine whether the characters in sub_s are in main_s
    # regardless of order
    sub = True
    for s in sub_s:
        if s not in main_s:
            sub = False
    return sub
    
def string_dif(str_a, str_b):
    # Returns the characters in str_a that are not in str_b
    return ''.join([i for i in str_a if i not in str_b])

def get_mappings(s_patterns):
    # Returns a dictionary with keys being digits and values
    # being the signals that comprise that digit
    
    mappings = {}
    s_patterns.sort(key=len)

    # Identify the unique ones first
    mappings[1] = s_patterns[0]
    mappings[7] = s_patterns[1]
    mappings[4] = s_patterns[2]
    mappings[8] = s_patterns[9]

    # Now we look at the 5-signal numbers: 2, 3, and 5
    
    # Number 5 will have the signals that are in 4 but not in 1
    test5 = string_dif(mappings[4], mappings[1])

    for s in range(3,6):
        if in_string(mappings[1], s_patterns[s]):
            # Number 3 will have all the signals from number 1
            mappings[3] = s_patterns[s] 
        elif in_string(test5, s_patterns[s]):
            mappings[5] = s_patterns[s]
        else:
            # If it's not a 3 or a 5, it's a 2
            mappings[2] = s_patterns[s]
    
    # Now we look at the 6-signal numbers: 6, 9, and 0
    
    # Number 6 will be missing the signal that is in 1 but not in 5
    # Number 9 will be missing the signal that is in 2 but not in 3
    test6 = string_dif(mappings[1], mappings[5])
    test9 = string_dif(mappings[2], mappings[3])
    
    for s in range(6,9):
        if test6 not in s_patterns[s]:
            mappings[6] = s_patterns[s]
        elif test9 not in s_patterns[s]:
            mappings[9] = s_patterns[s]
        else:
            mappings[0] = s_patterns[s]
        
    return mappings

total_value = 0

for this_input in my_input:
    this_value = ''
    m = get_mappings(this_input[0])
    for number in this_input[1]:
        for k in m:
            if m[k] == number:
                this_value += str(k)
                break
    total_value += int(this_value)

print("Part 2:", total_value)

