import math
import copy
from functools import reduce

def matches(line, rules, r):
  r = rules[r]

  if len(line) <= 0:
    return 0
  
  if "\"" in r[0]:
    if r[0][1] == line[0]:
      return 1
    else:
      return 0

  for x in r:
    offset = 0

    for y in x.split(" "):
      o = matches(line[offset:], rules, y)

      if o == 0:
        offset = 0
        break

      offset += o

    if offset != 0:
      return offset

  return 0

with open("input.txt", "r") as file:
  rules, messages = file.read().split("\n\n")

  # { '1': ['2 3', '3 2'] }
  rules = { k: v.split(" | ") for k, v in [r.split(": ") for r in rules.split("\n")] }

  print("solution =", sum([matches(m, rules, '0') == len(m) for m in messages.split("\n")]))