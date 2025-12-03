from time import perf_counter

with open('data.txt') as f: raw = f.read()

# We have a dial that is numbered 0-99, and a sequence of left/right turns to perform
# - The dial starts at position 50
# - The password is the number of times the dial stops on 0 after each step in the sequence
# Test data answer: 3

#raw = "L68\nL30\nR48\nL5\nR60\nL55\nL1\nL99\nR14\nL82"
data = raw.strip().split()

# Convert the L/R turn data into +/- ints for easier use
sequence = [int(('-' if s[:1] == 'L' else '') + s[1:]) for (s) in data]

start_time = perf_counter()
dial = 50
count = 0
for rotation in sequence:
    # Do the turns and shift the result back into the 0-99 range using modulo
    dial = (dial + rotation) % 100
    if dial == 0:
        count += 1

print('1. Password:', count, f"({round(perf_counter() - start_time,2)}s)")

########################################

# The password is the number of times the dial passes or stops on 0 during each step
# Test data answer: 6

start_time = perf_counter()
dial = 50
count = 0
# We are going to do each individual turn in each rotation of the sequence so we can count the 0s
for rotation in sequence:
    turn = 1 if rotation > 0 else -1
    for _ in range(abs(rotation)):
        dial = (dial + turn) % 100
        if dial == 0:
            count += 1

print('2. Password:', count, f"({round(perf_counter() - start_time,2)}s)")