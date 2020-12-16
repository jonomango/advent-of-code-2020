import math
from functools import reduce

def is_num_valid(num, field):
  r1, r2 = field[1]
  return (r1[0] <= num <= r1[1]) or (r2[0] <= num <= r2[1])

# remove tickets that are not valid
def validate(tickets, fields):
  new, invalid = [], []

  for t in tickets:
    valid = False

    for n in t:
      valid = False

      for f in fields:
        if not is_num_valid(n, f):
          continue

        # this num is valid
        valid = True
        break

      if not valid:
        invalid.append(n)
        break
    
    # this ticket is valid
    if valid:
      new.append(t)

  return new, invalid

with open("input.txt", "r") as file:
  fields, my_tickets, tickets = file.read().split("\n\n")

  # [["name", "0-1 or 1-2"], ...]
  fields = [x.split(": ") for x in fields.split("\n")]

  # { "name": [[min, max], [min, max]], ... }
  fields = [[name, [list(map(int, x.split("-"))) for x in values.split(" or ")]] for name, values in fields ]
  
  # [1, 2, 3]
  my_ticket = [int(x) for x in my_tickets[13:].split(",")]

  # [[1, 2, 3], ...]
  tickets = [[int(y) for y in x.split(",")] for x in tickets[16:].split("\n")]

  _, invalid = validate(tickets, fields)
  print("solution =", sum(invalid))