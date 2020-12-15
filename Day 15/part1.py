import math
from functools import reduce

nums = []

with open("input.txt", "r") as file:
  # iterate over every line in a file
  for n in [l.replace("\n", "") for l in file.read().split(",")]:
    nums.append(int(n))

for _ in range(len(nums), 2020):
  if nums[-1] not in nums[:-1]:
    nums.append(0)
  else:
    nums.append(nums[:-1][::-1].index(nums[-1]) + 1)
  

print("solution =", nums[-1])