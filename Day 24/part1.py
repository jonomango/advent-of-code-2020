import math
import copy
from functools import reduce

with open("input.txt", "r") as file:
  positions = []

  # iterate over every line in a file
  for line in file.read().strip().split("\n"):
    P = [0, 0]

    i = 0
    while i < len(line):
      # e, se, sw, w, nw, and ne
      if line[i] == "e":
        i += 1
        P[0] += 1
      elif line[i] == "w":
        i += 1
        P[0] -= 1
      elif line[i:i+2] == "se":
        i += 2
        P[0] += 0.5
        P[1] -= 0.5
      elif line[i:i+2] == "nw":
        P[0] -= 0.5
        i += 2
        P[1] += 0.5
      elif line[i:i+2] == "sw":
        i += 2
        P[0] -= 0.5
        P[1] -= 0.5
      elif line[i:i+2] == "ne":
        i += 2
        P[0] += 0.5
        P[1] += 0.5

    positions.append((P[0], P[1]))

  # white = True
  state = {}

  for P in positions:
    if P not in state:
      # black
      state[P] = False
    else:
      state[P] = not state[P]

  print(sum(not x for x in state.values()))