from math import sqrt
from collections import defaultdict

filename = 'puzzle_input/day19.txt'
#filename = 'puzzle_input/test_input.txt'

my_input = []
scanners = {}
with open(filename) as file:
    for line in file:
        if line.strip() == '':
            scanners[current_scanner] = this_set
        elif line[1] == '-':
            this_set = []
            current_scanner = int(line.strip().split()[2])
        else:
            this_coord = tuple([int(i) for i in line.strip().split(',')])
            this_set.append(this_coord)
    scanners[current_scanner] = this_set
    
def distance(a, b):
    xa, ya, za = a
    xb, yb, zb = b
    
    return round(sqrt((xa - xb) ** 2 + (ya - yb) ** 2 + (za - zb) ** 2),3)
        
'''for s in scanners:
    print("------------Scanner", s)
    for c in scanners[s]:
        print(c)
    print()'''
    
n = (0, 0, 0)
m = (1, 1, 0)

distance_list = defaultdict(int)
distances = {}
for s in scanners:
    for i in range(1, len(scanners[s])):
        d = distance(scanners[s][i], scanners[s][i-1])
        distance_list[d] += 1

for d in distance_list:
    test = distance_list[d]
    if test > 1:
        print(d, test)
        
#42 is wrong
