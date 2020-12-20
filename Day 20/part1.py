import math
import copy
from functools import reduce


def adjacent(tiles, tile):
  count = 0

  for b_outer in tile[1]:
    for tid, b in tiles.items():
      if tid == tile[0]:
        continue

      for b_inner in b:
        if b_outer == b_inner or b_outer == b_inner[::-1]:
          count += 1

  return count

def corners(tiles):
  corners = []

  for tile in tiles.items():
    # corners
    if adjacent(tiles, tile) == 2:
      corners.append(tile[0])

  return corners

with open("input.txt", "r") as file:
  tiles = {}

  # iterate over every line in a file
  for tile in file.read().split("\n\n"):
    tile_id, data = tile.split(":\n")

    tile_id = int(tile_id[5:])
    data = data.split("\n")

    borders = []
    borders.append(data[0])
    borders.append("".join([data[y][len(data[0]) - 1] for y in range(len(data))]))
    borders.append(data[len(data) - 1])
    borders.append("".join([data[y][0] for y in range(len(data))]))

    tiles[tile_id] = borders

  P = 1
  for x in corners(tiles):
    P *= x

  print("solution =", P)