import math
from functools import reduce

nums = []

with open("input.txt", "r") as file:
  # iterate over every line in a file
  for n in [l.replace("\n", "") for l in file.read().split(",")]:
    nums.append(int(n))

# stores the last known index of a number
table = {}

for i in range(len(nums) - 1):
  table[nums[i]] = i

for i in range(len(nums), 30000000):
  last = nums[-1]

  if last not in table:
    nums.append(0)
  else:
    nums.append(i - table[last] - 1)

  table[last] = i - 1
  
print("solution =", nums[-1])