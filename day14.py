from collections import defaultdict, Counter

filename = 'puzzle_input/day14.txt'
#filename = 'puzzle_input/test_input.txt'

# We will keep track of everything in dictionaries. Since we don't need
# the full polymer, we just track the pairs, elements, and their counts

insertion_rules = {}                # E.g rule AB -> C: key=AB, value=C
current_pairs = defaultdict(int)    # E.g key=AB, value=integer
element_count = defaultdict(int)    # E.g key=A, value=integer


# Process input
with open(filename) as file:
    polymer_template = file.readline().strip()
    
    for line in file:
        if line.strip() != '':    # Skip the blank line
            pair, element = line.strip().split(' -> ')
            insertion_rules[pair] = element

# Use polymer_template to populate the initial dictionary of pairs
for c in range(0, len(polymer_template) - 1):
    this_pair = polymer_template[c:c+2]
    current_pairs[this_pair] += 1

element_count = Counter(polymer_template)
steps = 40

for i in range(0, steps):
    new_pairs = defaultdict(int)    # Put all the pairs from this step here
    # Each pair acts exactly the same on each step. So we don't need the order
    # in the larger string. Just the pair and the count of each unique pair
    for this_pair in current_pairs:
        new_element = insertion_rules[this_pair]
        
        # Create 2 new pairs from the insertion rules. For example, AB -> C
        # changes pair AB into 2 new pairs: AC and CB.
        new1 = this_pair[0] + new_element
        new2 = new_element + this_pair[1]
        
        # Add the 2 new pairs to the new_pair dict. Their count is equal to the
        # old pair. So 25 ABs result in 25 ACs and 25 CBs.
        new_pairs[new1] += current_pairs[this_pair]
        new_pairs[new2] += current_pairs[this_pair]
        
        # The only new character we've added to the overall string is the new
        # added element. The quantity is the same as the pair that generated it
        # For example, 25 ABs will generate 25 new Cs if the rule is AB -> C
        element_count[new_element] += current_pairs[this_pair]
    current_pairs = new_pairs

print(max(element_count.values()) - min(element_count.values()))

