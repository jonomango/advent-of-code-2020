arr = []

with open("input.txt", "r") as f:
  for line in f.readlines():
    arr.append(int(line))

for a in arr:
  for b in arr:
    for c in arr:
      if a == b == c:
        continue

      if a + b + c == 2020:
        print(a * b * c)