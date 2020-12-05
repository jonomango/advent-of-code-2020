def bsp(start, instructions):
  mn, mx = 0, start
  
  for instr in instructions:
    if instr == "F" or instr == "L":
      mx = (mx - mn + 1) / 2 - 1 + mn
    else:
      mn += (mx - mn + 1) / 2

  return int(mn)

seats = [False for x in range(128 * 8)]

with open("input.txt", "r") as file:
  for line in file.readlines():
    row, column = bsp(127, line[:7]), bsp(7, line[7:-1])
    seats[row * 8 + column] = True

for i in range(128 * 8):
  if not seats[i] and seats[i - 1] and seats[i + 1]:
    print(i)