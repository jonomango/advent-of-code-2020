trees = []

with open("input.txt", "r") as f:
  for line in f.readlines():
    trees.append(line[:-1])

def calc_trees(slopex, slopey):
  # curr pos
  x, y = 0, 0

  count = 0

  while True:
    x += slopex
    y += slopey

    if y >= len(trees):
      break

    if trees[y][x % len(trees[y])] == '#':
      count += 1

  return count

slopes = [
  [1, 1], 
  [3, 1],
  [5, 1],
  [7, 1],
  [1, 2]]

product = 1

for slope in slopes:
  product *= calc_trees(slope[0], slope[1])

print(product)