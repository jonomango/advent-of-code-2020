import math
import copy
from functools import reduce

def adjacent(P):
  return (
    (P[0] + 1, P[1]),
    (P[0] - 1, P[1]),
    (P[0] + 0.5, P[1] + 0.5),
    (P[0] - 0.5, P[1] - 0.5),
    (P[0] + 0.5, P[1] - 0.5),
    (P[0] - 0.5, P[1] + 0.5)
  )

def adjacent_black(P, state):
  count = 0

  for A in adjacent(P):
    if A in state:
      count += 1

  return count

def simulate(state):
  new_state = {}

  # iterate over every black tile
  for P, _ in state.items():
    adj = adjacent_black(P, state)

    # Any black tile with zero or more than 2 black tiles immediately adjacent to it is flipped to white
    if not (adj == 0 or adj > 2):
      new_state[P] = True

    # iterate over every white tile
    for p2 in adjacent(P):
      if p2 in state:
        continue

      adj = adjacent_black(p2, state)

      # Any white tile with exactly 2 black tiles immediately adjacent to it is flipped to black
      if adj == 2:
        new_state[p2] = True

  return new_state

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
        i += 2
        P[0] -= 0.5
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

  # black = True
  state = {}

  for P in positions:
    if P not in state:
      # black
      state[P] = True
    else:
      del state[P]

  for _ in range(100):
    state = simulate(state)

  print(sum(1 for x in state))

