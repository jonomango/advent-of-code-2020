arr = []

with open("input.txt", "r") as f:
  for line in f.readlines():
    arr.append(int(line))

for a in arr:
  for b in arr:
    if a == b:
      continue

    if a + b == 2020:
      print(a * b)