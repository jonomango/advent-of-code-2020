import copy

seats = []

with open("input.txt", "r") as file:
  for line in file.readlines():
    seats.append(line.replace("\n", ""))

# try to find the nearest seat in the given direction
def get_seat_state(i, j, di, dj):
  while True:
    i += di
    j += dj

    if i < 0 or j < 0 or i >= len(seats) or j >= len(seats[i]):
      return "."

    if seats[i][j] != ".":
      return seats[i][j]

  return "L"

def nearby_occupied(i, j):
  occupied = 0

  # every direction
  for di in range(-1, 2):
    for dj in range(-1, 2):
      if di == 0 and dj == 0:
        continue

      if get_seat_state(i, j, di, dj) == "#":
        occupied += 1

  return occupied

def occupy_seats():
  new_seats = copy.deepcopy(seats)
  changed = False

  for i in range(len(seats)):
    for j in range(len(seats[i])):
      if seats[i][j] == "L" and nearby_occupied(i, j) == 0:
        new_seats[i] = new_seats[i][:j] + "#" + new_seats[i][j + 1:]
        changed = True
      if seats[i][j] == "#" and nearby_occupied(i, j) >= 5:
        new_seats[i] = new_seats[i][:j] + "L" + new_seats[i][j + 1:]
        changed = True

  return changed, new_seats

while True:
  c, seats = occupy_seats()
  if not c:
    break

print(sum([sum([x == "#" for x in row]) for row in seats]))