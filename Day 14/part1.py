import math
from functools import reduce

mem = {}
mask = ""

def set_value(address, value):
  for i, bit in enumerate(mask):
    if bit == "1":
      value |= 1 << (35 - i)
    elif bit == "0":
      value &= ~(1 << (35 - i))
  mem[address] = value

with open("input.txt", "r") as file:
  for line in file.readlines():
    line = line.replace("\n", "")

    # set the mask
    if line[:4] == "mask":
      mask = line[7:]

    # memset
    else:
      address, value = [int(x) for x in line[4:].split("] = ")]
      set_value(address, value)

print(sum([x for _, x in mem.items()]))