from time import perf_counter
import math
import re
#from tqdm import tqdm

with open('data.txt') as f: raw = f.read()

# A list of math problems laid out columns:
#   |123 328  51 64 |
#   | 45 64  387 23 |
#   |  6 98  215 314|
#   |*   +   *   +  |
# - The math operation is indicated by the last row
# - Perform the operation on the numbers in each colum, e.g.: 123 * 45 * 6
# - Problems are seperated by columns of blank spaces
# - Find the sum of the results of all problems
# Test data answer: 4277556

#raw = """123 328  51 64\n 45 64  387 23\n  6 98  215 314\n*   +   *   +  """

start_time = perf_counter()

data = raw.splitlines()

# Find the column ranges for each math problem.
# Note that the math function row data width cannot be trusted (width is less than the number data)
col_spans = [list(match.span()) for match in re.finditer(r"\S *", data[-1])]
col_spans[-1][1] = len(data[0])+1

# First, we split each line up into columns for each math problem. This way we keep the alignment padding!
# Then we "rotate" the data so that each problem is in its own array
data = [[r[span[0]:span[1]-1] for span in col_spans] for r in data]
data = [[data[j][i] for j in range(len(data))] for i in range(len(data[0]))]

# I did originally put all of this in a single monster list comprehension, but it wasn't very readable
def solve_problem(numbers, op):
    return sum(numbers) if op == "+" else math.prod(numbers)

result = 0
for problem in data:
    nums = map(int, problem[0:-1])
    result += solve_problem(nums, problem[-1].strip())

print('1. Sum of all math problems:', result, f"({round(perf_counter() - start_time,2)}s)")

###############################################################################

# Given the same data, read the numbers in each problem in columns, left-to-right, top-to-bottom
#   |123 328  51 64 |
#   | 45 64  387 23 |
#   |  6 98  215 314|
#   |*   +   *   +  |
# e.g. first problem: 356 * 24 * 1
# Test data answer: 3263827

start_time = perf_counter()

# We will unzip (zip(*var)) to convert the rows into lists of the numbers from each column:
#   |123|
#   | 45|  =>  [1, 24, 356]
#   |  6|

result = 0
for problem in data:
    nums = [int("".join(n).strip()) for n in zip(*problem[:-1])]
    print(nums)
    result += solve_problem(nums, problem[-1].strip())

print('2. Sum of column problems:', result, f"({round(perf_counter() - start_time,2)}s)")