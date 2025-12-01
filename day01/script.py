with open('data.txt') as f: raw = f.read()
#raw = "L68\nL30\nR48\nL5\nR60\nL55\nL1\nL99\nR14\nL82"
data = raw.strip().split()
turns = [int(('-' if s[:1] == 'L' else '') + s[1:]) for (s) in data]

dial = 50
count = 0
for turn in turns:
    dial += turn
    while dial > 99:
        dial -= 100
    while dial < 0:
        dial += 100
    if dial == 0:
        count += 1

print('1.',count)

dial = 50
count = 0
for turn in turns:
    step = 1 if turn > 0 else -1
    for _ in range(abs(turn)):
        dial += step
        if dial < 0:
            dial += 100
        elif dial > 99:
            dial -= 100
        if dial == 0:
            count += 1

print('2.',count)