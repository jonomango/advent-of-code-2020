import copy

seats = []

with open("input.txt", "r") as file:
  for line in file.readlines():
    seats.append(line.replace("\n", ""))

def nearby_occupied(i, j):
  occupied = 0

  if i + 1 < len(seats) and seats[i + 1][j] == "#":
    occupied += 1
  if i - 1 >= 0 and seats[i - 1][j] == "#":
    occupied += 1
  if j + 1 < len(seats[i]) and seats[i][j + 1] == "#":
    occupied += 1
  if j - 1 >= 0 and seats[i][j - 1] == "#":
    occupied += 1

  if i + 1 < len(seats) and j + 1 < len(seats[i + 1]) and seats[i + 1][j + 1] == "#":
    occupied += 1
  if i - 1 >= 0 and j + 1 < len(seats[i - 1]) and seats[i - 1][j + 1] == "#":
    occupied += 1

  if i + 1 < len(seats) and j - 1 >= 0 and seats[i + 1][j - 1] == "#":
    occupied += 1
  if i - 1 >= 0 and j - 1 >= 0 and seats[i - 1][j - 1] == "#":
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
      if seats[i][j] == "#" and nearby_occupied(i, j) >= 4:
        new_seats[i] = new_seats[i][:j] + "L" + new_seats[i][j + 1:]
        changed = True

  return changed, new_seats

while True:
  c, seats = occupy_seats()
  if not c:
    break

print(sum([sum([x == "#" for x in row]) for row in seats]))