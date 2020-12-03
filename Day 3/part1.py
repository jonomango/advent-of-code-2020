trees = []

with open("input.txt", "r") as f:
  for line in f.readlines():
    trees.append(line[:-1])

# curr pos
x, y = 0, 0

count = 0

while True:
  x += 3
  y += 1

  if y >= len(trees):
    break

  if trees[y][x % len(trees[y])] == '#':
    count += 1

print(count)