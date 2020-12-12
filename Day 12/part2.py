import math

instructions = []

with open("input.txt", "r") as file:
  for line in file.readlines():
    instructions.append([line[0], int(line[1:])])

def rotate(x, y, angle):
  return x * int(math.cos(math.radians(-angle))) - y * int(math.sin(math.radians(-angle))),\
         x * int(math.sin(math.radians(-angle))) + y * int(math.cos(math.radians(-angle)))

x, y = 0, 0

# delta between waypoint and ship
dx, dy = 10, 1

for op, value in instructions:
  if op == "N":
    dy += value
  elif op == "S":
    dy -= value
  elif op == "E":
    dx += value
  elif op == "W":
    dx -= value
  elif op == "F":
    x += dx * value
    y += dy * value
  elif op == "R":
    dx, dy = rotate(dx, dy, value)
  elif op == "L":
    dx, dy = rotate(dx, dy, -value)

print(abs(x) + abs(y))