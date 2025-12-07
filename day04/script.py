from time import perf_counter
#from tqdm import tqdm
#import re

with open('data.txt') as f: raw = f.read()

# Find every paper roll (@) that is surrounded by fewer than 4 other rolls
# - Check every cell surrounding: to the left, right, above, below and the 4 diagonals
# Test data number of rolls: 13

#raw = "..@@.@@@@.\n@@@.@.@.@@\n@@@@@.@.@@\n@.@@@@..@.\n@@.@@@@.@@\n.@@@@@@@.@\n.@.@.@.@@@\n@.@@@.@@@@\n.@@@@@@@@.\n@.@.@@@.@."

data = [list("."+s+".") for (s) in raw.strip().split()]
# Add margins to the data grid so we don't have to do edge checks
data.insert(0, list("."*len(data[0])))
data.append(list("."*len(data[0])))

start_time = perf_counter()

# We will use this map of offsets to look up adjacent cells
adjacents = [[-1, -1], [-1, 0], [-1, 1],
             [ 0, -1],          [ 0, 1],
             [ 1, -1], [ 1, 0], [ 1, 1]]

# Function to return a list of (row,col) positions for all rolls with fewer than 4 adjacent rolls
def get_accessible_rolls():
    roll_positions = []
    width = len(data[0])-1
    for row_ind in range(1, len(data)-1):
        for col_ind in range(1, width):
            if data[row_ind][col_ind] == ".": continue
            # Using the adjacent offsets, collect a list of all surrounding rolls
            surrounding_papers = [int(data[row_ind + offset[0]][col_ind + offset[1]] == "@") for (offset) in adjacents]
            if sum(surrounding_papers) < 4:
                roll_positions.append([row_ind, col_ind])
    return roll_positions

accessible_roll_count = len(get_accessible_rolls())
print('1. Total accessible rolls:', accessible_roll_count, f"({round(perf_counter() - start_time,2)}s)")

###############################################################################

# Repeatedly remove all paper rolls with fewer than 4 other rolls surrounding them
# - How many paper rolls can be removed?
# Test data total removed rolls: 43

start_time = perf_counter()

# Repeatedly remove rolls from the data until no more can be removed
removed_rolls = 0
while True:
    accessible_rolls = get_accessible_rolls()
    if len(accessible_rolls) == 0: break
    for roll in accessible_rolls:
        data[roll[0]][roll[1]] = "."
    removed_rolls += len(accessible_rolls)

print('2. Total rolls that can be removed:', removed_rolls, f"({round(perf_counter() - start_time,2)}s)")