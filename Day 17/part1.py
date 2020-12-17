import math
import copy
from functools import reduce

def nearby(coords):
  arr = []

  for x in range(coords[0] - 1, coords[0] + 2):
    for y in range(coords[1] - 1, coords[1] + 2):
      for z in range(coords[2] - 1, coords[2] + 2):
        arr.append((x, y, z))

  return arr

def num_active(coords, states, memoize):
  if coords in memoize:
    return memoize[coords]

  num = 0

  for c in nearby(coords):
    if c != coords and c in states and states[c] == "#":
      num += 1

  memoize[coords] = num
  return num

def process_states(states):
  new_states = {}
  memoize = {}

  for coords in states:
    for c in nearby(coords):
      # already calculated
      if c in new_states:
        continue

      active = num_active(c, states, memoize)

      # the value of the cube
      v = "."
      if c in states:
        v = states[c]

      if v == "#" and not (active == 2 or active == 3):
        v = "."
      if v == "." and active == 3:
        v = "#"

      # we really only care about active states
      if v != ".":
        new_states[c] = v

  return new_states

with open("input.txt", "r") as file:
  # { (x, y, z): value }
  states = {}

  y = 0

  # iterate over every line in a file
  for line in [l.replace("\n", "") for l in file.readlines()]:
    for x in range(len(line)):
      states[(x, y, 0)] = line[x]

    y += 1

  for c in range(6):
    states = process_states(states)
    print("cycle", c + 1, "finished")

  print("solution:", sum([x == "#" for x in states.values()]))