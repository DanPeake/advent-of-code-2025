from time import perf_counter
#from tqdm import tqdm
#import re

with open('data.txt') as f: raw = f.read()

# Given data that is split into two sections, seperated by a blank line:
# - The first section of data lists various ID ranges of "fresh ingredients"
# - Ranges can overlap
# - The second section of data lists individual ingredient IDs
# - Find the number of ingredient IDs that are in the "fresh" ranges
# Test data answer: 3

# raw = "3-5\n10-14\n16-20\n12-18\n\n1\n5\n8\n11\n17\n32"

start_time = perf_counter()

# Split the data into two variables, one for ranges, one for ingredients
fresh_end = raw.find('\n\n')
fresh_ranges = [[int(id) for (id) in r.split('-')] for (r) in raw[:fresh_end].strip().split()]
ingredients = [int(id) for id in raw[fresh_end:].strip().split()]

# Returns true if the given ID is in a fresh range
def is_fresh(id):
    for test_range in fresh_ranges:
        if test_range[0] <= id <= test_range[1]:
            return True
    return False

fresh_ingredients = [int(is_fresh(id)) for (id) in ingredients]

print('1. Number of fresh ingredients:', sum(fresh_ingredients), f"({round(perf_counter() - start_time,2)}s)")

###############################################################################

# Ignoring the ingredient IDs, find the total number of unique "fresh" IDs in all ranges
# - Ranges can overlap
# Test data answer: 14

start_time = perf_counter()

# Sort the ranges so that we can easily combine ranges
fresh_ranges.sort(key=lambda x: [x[0],x[1]])

# Compare the current range with the next one, and combine them if the overlap
def combine_ranges(range_list):
    combined_ranges = [range_list[0]]
    for i in range(1, len(range_list)):
        a = combined_ranges[-1]
        b = range_list[i]
        if b[0] <= a[1]:
            combined_ranges[-1] = [a[0], max(a[1], b[1])]
        else:
            combined_ranges.append(b)
    return combined_ranges

count = sum([x[1]-x[0]+1 for (x) in combine_ranges(fresh_ranges)])
print('2. Total fresh IDs:', count, f"({round(perf_counter() - start_time,2)}s)")