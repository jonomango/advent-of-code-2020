import math
import copy
from functools import reduce

with open("input.txt", "r") as file:
  p1, p2 = file.read().strip().split("\n\n")
  p1 = list(map(int, p1[10:].split("\n")))
  p2 = list(map(int, p2[10:].split("\n")))

  while len(p1) != 0 and len(p2) != 0:
    c1, c2 = p1[0], p2[0]
    p1, p2 = p1[1:], p2[1:]

    if c1 > c2:
      p1 += [c1, c2]
    else:
      p2 += [c2, c1]

  print(sum(x * (i + 1) for i, x in enumerate(p1[::-1])))
  print(p1, p2)