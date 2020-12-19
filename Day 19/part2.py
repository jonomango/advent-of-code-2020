import math
import copy
from functools import reduce

def matches(line, rules, rule):
  # this is the base case
  if "\"" in rule:
    if len(line) > 0 and line[0] == rule[1]:
      return [1]
    else:
      return []

  # rule = ['1', '2']
  rule = rule.split(" ")

  # this stores the possible offsets from line[0:] that match
  offsets = []

  for i in range(len(rule)):
    r = rule[i]
    r = rules[r]

    # first iteration, offsets is empty
    if i == 0:
      for s in r:
        for m in matches(line, rules, s):
          if m not in offsets:
            offsets.append(m)
      continue

    new_offsets = []

    for s in r:
      for o in offsets:
        for m in matches(line[o:], rules, s):
          new_offsets.append(o + m)

    offsets = new_offsets

  return offsets

with open("input.txt", "r") as file:
  rules, messages = file.read().split("\n\n")

  # { '1': ['2 3', '3 2'] }
  rules = { k: v.split(" | ") for k, v in [r.split(": ") for r in rules.split("\n")] }

  rules['8'] = ['42', '42 8']
  rules['11'] = ['42 31', '42 11 31']

  #print("result:", matches(messages.split("\n")[0], rules, '1'))
  print("solution =", sum([len(m) in matches(m, rules, '0') for m in messages.split("\n")]))