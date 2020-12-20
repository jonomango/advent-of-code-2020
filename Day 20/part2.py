import math
import copy
from functools import reduce

monster = [
  "                  # ",
  "#    ##    ##    ###",
  " #  #  #  #  #  #   ",
]

# flip an array of data over the x-axis (or y-axis)
def flip(data, xaxis):
  if xaxis:
    return data[::-1]
  else:
    return [row[::-1] for row in data]

# rotate an array of data clockwise
def rotate(data, r):
  r %= 4

  # bruh
  if r == 0:
    return data
  # 90 degrees
  elif r == 1:
    return ["".join(row[i] for row in data[::-1]) for i in range(len(data))]
  # 180 degrees
  elif r == 2:
    return [row[::-1] for row in data[::-1]]
  # 270 degrees
  else:
    return ["".join(row[-i - 1] for row in data) for i in range(len(data))]

# rotate and flip according to input
def transform(data, face1, face2, should_flip):
  data = rotate(data, face1 - face2 + 2)

  if should_flip:
    data = flip(data, face1 % 2)
  
  return data

# get the 4 borders of a square
def borders(data):
  return [
    data[0],
    "".join(row[-1] for row in data),
    data[-1][::-1],
    "".join(row[0] for row in data[::-1]),
  ]

# returns a list of adjecent tiles
# (id, face1, face2, flip)
def adjacent(tiles, tid):
  adj = []
  data = tiles[tid]

  for i, d in tiles.items():
    # ignore ourself
    if i == tid:
      continue

    for s1, b1 in enumerate(borders(data)):
      for s2, b2 in enumerate(borders(d)):
        # matches, but needs to flip
        if b1 == b2:
          adj.append((i, s1, s2, True))
        # no need to flip
        elif b1 == b2[::-1]:
          adj.append((i, s1, s2, False))

  return adj

# get a corner tile id
def corner(tiles):
  for tid in tiles:
    adj = adjacent(tiles, tid)

    # corners
    if len(adj) == 2:
      # side length
      side = int(math.sqrt(len(tiles)))

      x, y = 0, 0

      if 0 not in [i for _, i, _, _ in adj]:
        y = side - 1

      if 1 not in [i for _, i, _, _ in adj]:
        x = side - 1

      return tid, x, y

  return None

# make a 2D array image
def form_image(tiles):
  # side length
  side = int(math.sqrt(len(tiles)))

  # start processing from a corner
  # (id, x, y)
  to_process = [corner(tiles)]

  # note: (x, y) coords are grid[y][x] and grid[0][0] is top left
  grid = [[None for _ in range(side)] for _ in range(side)]
  grid[to_process[0][2]][to_process[0][1]] = to_process[0][0]

  for curr_id, curr_x, curr_y in to_process:
    # process adjacent tiles
    for adj_id, face1, face2, should_flip in adjacent(tiles, curr_id):
      # already processed
      if adj_id in [x for row in grid for x in row]:
        continue

      # transform the tile so that it actually fits
      tiles[adj_id] = transform(tiles[adj_id], face1, face2, should_flip)

      x, y = curr_x, curr_y

      if face1 == 0:
        y += 1
      elif face1 == 1:
        x += 1
      elif face1 == 2:
        y -= 1
      else:
        x -= 1
      
      grid[y][x] = adj_id
      to_process.append((adj_id, x, y))

  image = []

  tile_length = len(list(tiles.values())[0])

  # at this point, grid is an array of properly placed ids
  # and every tile in tiles is properly sorted
  for row in grid:

    for i in range(1, tile_length - 1):
      image.append("")

      for tid in row:
        image[-1] += tiles[tid][-i - 1][1:-1]

  return image

# check if this matches the monster
def matches(image, xoff, yoff):
  # check if matches
  for i in range(len(monster[0])):
    for j in range(len(monster)):
      # we only care about this shit
      if monster[j][i] != "#":
        continue

      if image[j + yoff][i + xoff] != "#":
        return False

  return True

# mark monsters in an image
def mark_monsters(image, inhabited):
  for xoff in range(len(image) - len(monster[0])):
    for yoff in range(len(image) - len(monster)):
      if not matches(image, xoff, yoff):
        continue

      for i in range(len(monster[0])):
        for j in range(len(monster)):
          # we only care about this shit
          if monster[j][i] != "#":
            continue

          inhabited[(xoff + i, yoff + j)] = None

with open("input.txt", "r") as file:
  tiles = {}

  # iterate over every line in a file
  for tile in file.read().split("\n\n"):
    tile_id, data = tile.split(":\n")

    # add to dict
    tiles[int(tile_id[5:])] = data.split("\n")

  image = form_image(tiles)
  inhabited = {}

  for _ in range(4):
    image = rotate(image, 1)
    mark_monsters(image, inhabited)

  image = flip(image, True)

  for _ in range(4):
    image = rotate(image, 1)
    mark_monsters(image, inhabited)

  print("solution:", sum(row.count("#") for row in image) - len(inhabited))