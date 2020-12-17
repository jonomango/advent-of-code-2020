import math
import copy
from functools import reduce

with open("input2.txt", "r") as file:
  # iterate over every line in a file
  for line in [l.replace("\n", "") for l in file.readlines()]:
    print(line)

print("solution =", 69)