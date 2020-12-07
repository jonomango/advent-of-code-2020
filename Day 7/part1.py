bags = []

with open("input.txt", "r") as file:
  for line in file.readlines():
    line = line.replace("no", "0").replace("\n", "")

    container, contents = line[:-1].split(" bags contain ")
    contents = contents.replace(" bags", "").replace(" bag", "")

    # [["name", amount]]
    contents = [[x[x.index(" ") + 1:], int(x[:x.index(" ")])] for x in contents.split(", ")]

    bags.append([container, contents])

def recurse(targets):
  possible = []

  for bag, contents in bags:
    for child, capacity in contents:
      if capacity <= 0:
        continue

      if child in targets:
        possible.append(bag)
        break

  return possible

targets = ["shiny gold"]
previous = []

while len(targets) > 0:
  targets = recurse(targets)
  
  for x in targets:
    if x not in previous:
      previous.append(x)

print(len(previous))