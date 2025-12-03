from time import perf_counter
#from tqdm import tqdm
#import re

with open('data.txt') as f: raw = f.read()

# Find the largest possible combination of 2 digits in each row
# - Digits must be combined in the order they appear
# - Answer is the sum of the largest combination number from each row
# Test data answers: 98 + 89 + 78 + 92 = 357

#raw = "987654321111111\n811111111111119\n234234234234278\n818181911112111"
data = raw.strip().split()

start_time = perf_counter()

# Finds the largest digit in a row, repeating for the number of digits requested in the output
# Each time it repeats, it starts looking from the position of the last selected largest digit
# It does not check the whole row - it will reserve digits at the end of the row so it cannot run out later
def get_largest_combo(row, digits):
    largest_ind = 0
    combo = ""
    row_size = len(row)+1
    for step in range(digits):
        # Scans starting from the digit after the previous selected digit
        # It needs to find the requested number of digits:
        # It scans up to a point where the number of digits it needs to fill remain in the row
        for current_ind in range(largest_ind+1, row_size-(digits-step)):
            if row[current_ind] > row[largest_ind]:
                largest_ind = current_ind
        combo += row[largest_ind]
        largest_ind += 1
    return int(combo)

sum = 0
for row in data:
    sum += get_largest_combo(row, 2)

print('1. Sum of largest 2-combo num in reach row:', sum, f"({round(perf_counter() - start_time,2)}s)")

########################################

# Now find 12 digits in each row
# Test data answers: 987654321111 + 811111111119 + 434234234278 + 888911112111 = 3121910778619

start_time = perf_counter()

sum = 0
for row in data:
    sum += get_largest_combo(row, 12)

print('2. Sum of largest 12-combo num in reach row:', sum, f"({round(perf_counter() - start_time,2)}s)")