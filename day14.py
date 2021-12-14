from collections import defaultdict

filename = 'puzzle_input/day14.txt'
#filename = 'puzzle_input/test_input.txt'

insertion_rules = {}
current_pairs = defaultdict(int)
element_count = defaultdict(int)
steps = 40

with open(filename) as file:
    polymer_template = file.readline().strip()
    
    for line in file:
        if line.strip() != '':
            pair, element = line.strip().split(' -> ')
            insertion_rules[pair] = element

for c in range(0, len(polymer_template) - 1):
    this_pair = polymer_template[c] + polymer_template[c + 1]
    current_pairs[this_pair] += 1
    element_count[polymer_template[c]] += 1
    
element_count[polymer_template[-1]] += 1

new_pairs = defaultdict(int)

def do_step(c_pairs, e_count, i_rules):
    new_pairs = defaultdict(int)
    for this_pair in c_pairs:
        if this_pair in i_rules:
            new_element = i_rules[this_pair]
            new1 = this_pair[0] + new_element
            new2 = new_element + this_pair[1]
            new_pairs[new1] += c_pairs[this_pair]
            new_pairs[new2] += c_pairs[this_pair]
            e_count[new_element] += c_pairs[this_pair]
        else:
            new_pairs[this_pair] = c_pairs[this_pair]
    return new_pairs

for i in range(0, steps):
    current_pairs = do_step(current_pairs, element_count, insertion_rules)

max_quantity = 0
min_quantity = None

for e in element_count:
    c = element_count[e]
    if min_quantity is None or c < min_quantity:
        min_quantity = c
    if c > max_quantity:
        max_quantity = c

print(max_quantity - min_quantity)

