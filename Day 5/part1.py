def bsp(start, instructions):
  mn, mx = 0, start
  
  for instr in instructions:
    if instr == "F" or instr == "L":
      mx = (mx - mn + 1) / 2 - 1 + mn
    else:
      mn += (mx - mn + 1) / 2

  return int(mn)

largest = 0

with open("input.txt", "r") as file:
  for line in file.readlines():
    row, column = bsp(127, line[:7]), bsp(7, line[7:-1])
    largest = max(row * 8 + column, largest)

print(largest)