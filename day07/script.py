from time import perf_counter
import re
#from tqdm import tqdm

with open('data.txt') as f: raw = f.read()

# Starting from S and moving downward, a beam travels until it hits a splitter (^)
# - Upon hitting a splitter, it splits into 2 beams that continue to travel down
# - Count the number of times the beam splits
# Test data answer: 21

#raw = """.......S.......\n...............\n.......^.......\n...............\n......^.^......\n...............\n.....^.^.^.....\n...............\n....^.^...^....\n...............\n...^.^...^.^...\n...............\n..^...^.....^..\n...............\n.^.^.^.^.^...^.\n..............."""

start_time = perf_counter()

data = raw.splitlines()

# Keep track of each beam using a set (so that beams get automatically merged)
# Find all splitters in the current line, then check each beam and split it if it hit one of them
# Count each time a split happens
split_count = 0
beams = {data[0].find('S')}
for line in data[1:]:
    splitters = [match.start() for match in re.finditer(r'\^', line)]
    new_beams = set()
    for beam in beams:
        if beam in splitters:
            new_beams.update({beam+1, beam-1})
            split_count += 1
        else:
            new_beams.add(beam)
    beams = new_beams

print('1. Total beam splits:', split_count, f"({round(perf_counter() - start_time,2)}s)")

###############################################################################

# When a beam splits, it creates a new timeline
# Count the number of all possible timelines (i.e. beam paths)
# Test data answer: 40

start_time = perf_counter()

# Counting each beam individually is exponential and won't work
# Instead, we simply keep track of how many beams are passing through each splitter
# When beams from multiple splitters merge, we add to the count for that beam
# At the end, we just sum up the number of merged beams in each beam
beam_counts = {str(data[0].find('S')):1}
for line in data[1:]:
    splitters = [str(match.start()) for match in re.finditer(r'\^', line)]
    if len(splitters) == 0: continue
    new_beams = {}
    for beam, count in beam_counts.items():
        if beam in splitters:
            beam_left = str(int(beam) - 1)
            beam_right = str(int(beam) + 1)
            new_beams[beam_left] = new_beams.setdefault(beam_left, 0) + count
            new_beams[beam_right] = new_beams.setdefault(beam_right, 0) + count
        else:
            new_beams[beam] = new_beams.setdefault(beam, 0) + count
    beam_counts = new_beams

print('2. Total timelines:', sum(beam_counts.values()), f"({round(perf_counter() - start_time,2)}s)")