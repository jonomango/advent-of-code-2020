import math

instructions = []

with open("input.txt", "r") as file:
  for line in file.readlines():
    instructions.append([line[0], int(line[1:])])

x, y = 0, 0

# forward
angle = 90

for op, value in instructions:
  if op == "N":
    y += value
  elif op == "S":
    y -= value
  elif op == "E":
    x += value
  elif op == "W":
    x -= value
  elif op == "F":
    x += int(math.sin(math.radians(angle))) * value
    y += int(math.cos(math.radians(angle))) * value
  elif op == "R":
    angle += value
  elif op == "L":
    angle -= value

print(abs(x) +  abs(y))