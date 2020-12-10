adaptors = []

with open("input.txt", "r") as file:
  for line in file.readlines():
    adaptors.append(int(line))

adaptors.sort()

last, ones, threes = 0, 0, 1
for a in adaptors:
  if a - last == 1:
    ones += 1
  elif a - last == 3:
    threes += 1
  last = a

print(ones * threes)