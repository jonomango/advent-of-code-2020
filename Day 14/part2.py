import math
from functools import reduce

mem = {}
mask = ""

# recursively split an address into each possible combination
def recurse(addresses, index = 0):
  for i in range(index, 36):
    if mask[35 - i] != "X":
      continue

    newa = []

    for a in addresses:
      newa.append(a | (1 << i))
      newa.append(a & ~(1 << i))

    return recurse(newa, i + 1)

  return addresses

def set_value(address, value):
  for i, bit in enumerate(mask):
    if bit == "1":
      address |= 1 << (35 - i)

  for a in recurse([address]):
    mem[a] = value

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