from time import perf_counter
import re

with open('data.txt') as f: raw = f.read()

# Given a list of ID ranges (inclusive), find invalid IDs in each range
# - An invalid ID is one that is made of 2 identical halves: e.g. 123123
# - Answer is the sum of all invalid IDs
# Test data sum of invalid IDs: 1227775554

#raw = "11-22,95-115,998-1012,1188511880-1188511890,222220-222224,1698522-1698528,446443-446449,38593856-38593862,565653-565659,824824821-824824827,2121212118-2121212124"
data = raw.strip().split(',')
id_list = [s.split('-') for (s) in data]

start_time = perf_counter()
invalid_id_sum = 0
for id_range in id_list:
    for id in range(int(id_range[0]), int(id_range[1])+1):
        str_id = str(id)
        # Only IDs of even length can be invalid
        if len(str_id) % 2 == 0:
            # Check each half of the string against the other
            ind = len(str_id)//2
            if str_id[:ind] == str_id[ind:]:
                invalid_id_sum += id

print('1. Sum of double repeated IDs:', invalid_id_sum, f"({round(perf_counter() - start_time,2)}s)")

########################################

# An invalid ID is one that is filled with a pattern that repeats at least twice
# Test data sum of invalid IDs: 4174379265

start_time = perf_counter()
invalid_id_sum = 0
for id_range in id_list:
    for id in range(int(id_range[0]), int(id_range[1])+1):
        # Use regex to match: this captures a portion of the string, then checks if that group can be matched again
        if re.fullmatch(r"(.+)\1+", str(id)) is not None:
            invalid_id_sum += id

print('2. Sum of all repeat IDs:', invalid_id_sum, f"({round(perf_counter() - start_time,2)}s)")