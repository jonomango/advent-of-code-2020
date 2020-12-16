import math
from functools import reduce

def is_num_valid(num, field):
  r1, r2 = field[1]
  return (r1[0] <= num <= r1[1]) or (r2[0] <= num <= r2[1])

def is_column_valid(column, field):
  # special case when we invalidate a column and field
  if column == None or field == None:
    return False

  for n in column:
    if not is_num_valid(n, field):
      return False

  return True

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

# transpose a matrix
def transpose(matrix):
  mat = [[] for _ in matrix[0]]

  for i in range(len(matrix)):
    for j in range(len(matrix[i])):
      mat[j].append(matrix[i][j])

  return mat

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

  # remove invalid tickets
  tickets, _ = validate(tickets + [my_ticket], fields)

  # tickets[i] is a column
  tickets = transpose(tickets)

  p = 1

  for _ in range(len(fields)):
    # search for a field that is only valid for one column
    for i in range(len(fields)):
      # a list of indexes for valid columns
      valid_columns = []

      for j, column in enumerate(tickets):
        if is_column_valid(column, fields[i]):
          valid_columns.append(j)

      if len(valid_columns) != 1:
        continue

      column_index = valid_columns[0]
      if "departure" in fields[i][0]:
        p *= my_ticket[column_index]

      # make these invalid so that we dont get false positives
      fields[i] = None
      tickets[column_index] = None

      break

  print("solution =", p)