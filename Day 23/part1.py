import math
import copy
from functools import reduce

def normalize(dest, cups):
  if dest < min(cups + picked):
    dest = max(cups + picked)
  return dest

with open("input.txt", "r") as file:
  cups = list(map(int, file.read().strip()))
  count = 100

  for _ in range(count):
    picked = cups[1:4]
    cups = cups[:1] + cups[4:]

    dest = normalize(cups[0] - 1, cups)
    while dest in picked:
      dest = normalize(dest - 1, cups)
    
    dest = cups.index(dest) + 1
    cups = cups[:dest] + picked + cups[dest:]
    cups = cups[1:] + cups[:1]

  print("".join(map(str, (cups + cups)[cups.index(1) + 1:][:len(cups) - 1])))