"""
-------------------------------------------------------------------------------
This section is from redblobgames.com. I do not understand it. It is not mine.
Read more at https://redblobgames.com/pathfinding/a-star/implementation.html
RBG released it under Apache License 2.0: apache.org/licenses/LICENSE-2.0.html

I did remove parts of the code I didn't need such as checking for walls and all
the stuff about typing.
-------------------------------------------------------------------------------
"""

import heapq


class SquareGrid:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def in_bounds(self, id):
        (x, y) = id
        return 0 <= x < self.width and 0 <= y < self.height
        
    def neighbors(self, id):
        (x, y) = id
        neighbors = [(x+1, y), (x-1, y), (x, y-1), (x, y+1)]
        
        if (x + y) % 2 == 0:
            neighbors.reverse()
        results = filter(self.in_bounds, neighbors)
        
        return results


class GridWithWeights(SquareGrid):
    def __init__(self, width, height):
        super().__init__(width, height)
        self.weights = {}
    
    def cost(self, from_node, to_node):
        return self.weights.get(to_node, 1)


def heuristic(a, b):
    (x1, y1) = a
    (x2, y2) = b
    return abs(x1 - x2) + abs(y1 - y2)
    

class PriorityQueue:
    def __init__(self):
        self.elements = []
    
    def empty(self):
        return not self.elements
    
    def put(self, item, priority):
        heapq.heappush(self.elements, (priority, item))
    
    def get(self):
        return heapq.heappop(self.elements)[1]
        

def a_star_search(graph, start, goal):
    frontier = PriorityQueue()
    frontier.put(start, 0)
    came_from = {}
    cost_so_far = {}
    came_from[start] = None
    cost_so_far[start] = 0
    
    while not frontier.empty():
        current = frontier.get()
        
        if current == goal:
            break
        
        for next in graph.neighbors(current):
            new_cost = cost_so_far[current] + graph.cost(current, next)
            if next not in cost_so_far or new_cost < cost_so_far[next]:
                cost_so_far[next] = new_cost
                priority = new_cost + heuristic(next, goal)
                frontier.put(next, priority)
                came_from[next] = current
    
    return came_from, cost_so_far
    
"""
-------------------------------------------------------------------------------
OK here starts the code I actually wrote for myself. Everything above these
lines is lightly modified code borrowed from redblobgames.com
-------------------------------------------------------------------------------
"""

filename = 'puzzle_input/day15.txt'
#filename = 'puzzle_input/test_input.txt'

my_input = []

with open(filename) as file:
    for line in file:
        my_input.append(line.strip())

cavern_width = len(my_input[0])
cavern_height = len(my_input)
goal = (cavern_width-1, cavern_height-1)

# Create the GridWithWeights map
cavern_map = GridWithWeights(cavern_width, cavern_height)

# Add the weights
for x in range(cavern_width):
    for y in range(cavern_height):
        cavern_map.weights[(x, y)] = int(my_input[y][x])

# Calculate the path
_, path = a_star_search(cavern_map, (0, 0), goal)

print("Part 1:", path[goal])


def grid_increase(map_chunk):
    # Function to increase all the weights in a grid then return the grid
    new_grid = []
    for map_y in range(len(map_chunk)):
        new_line = ''
        for map_x in range(len(map_chunk[0])):
            # modular arithmetic to wrap around, but adding 1 because we're
            # starting at 1 instead of zero
            new_line += str((int(map_chunk[map_y][map_x])) % 9 + 1)
        new_grid.append(new_line)
    
    return new_grid


def connect_grid_lr(left_grid, right_grid):
    # Function to push together the left and right grid
    new_grid = []
    for y in range(len(left_grid)):
        new_line = left_grid[y] + right_grid[y]
        new_grid.append(new_line)
    return new_grid


def connect_grid_tb(top_grid, bottom_grid):
    # Function to glue together the top and bottom grid
    new_grid = []
    for y in top_grid:
        new_grid.append(y)
    for y in bottom_grid:
        new_grid.append(y)
    return new_grid

# First make 2 copies of my_input.
# Expanded_grid will be the final huge grid. New_grid will be for
# increasing the numbers by 1
expanded_grid = []
new_grid = []
for row in my_input:
    expanded_grid.append(row)
    new_grid.append(row)

# Repeatedly increase new_grid then attach it to expanded_grid
# This makes the first row in expanded_grid

# We already have the first chunk (new_grid) which is why we start at 1
for i in range(1, 5):
    new_grid = grid_increase(new_grid)
    expanded_grid = connect_grid_lr(expanded_grid, new_grid)

# Now we make a copy of expanded_grid and store it in new_grid
# We will increase this copy to create further rows
new_grid = []
for row in expanded_grid:
    new_grid.append(row)
    
# Repeatedly increase new_grid then attach it to expanded_grid
for i in range(1, 5):
    new_grid = grid_increase(new_grid)
    expanded_grid = connect_grid_tb(expanded_grid, new_grid)

# We're about ready to search. Set the width, height, and goal
cavern_width = len(expanded_grid[0])
cavern_height = len(expanded_grid)
goal = (cavern_width-1, cavern_height-1)

# Create the new GridWithWeights map
expanded_cavern_map = GridWithWeights(cavern_width, cavern_height)

# Set the weights
for x in range(cavern_width):
    for y in range(cavern_height):
        expanded_cavern_map.weights[(x, y)] = int(expanded_grid[y][x])

# Find the path!
_, path = a_star_search(expanded_cavern_map, (0, 0), goal)

print("Part 2:", path[goal])

