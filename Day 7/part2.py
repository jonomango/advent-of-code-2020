bags = []

with open("input.txt", "r") as file:
  for line in file.readlines():
    line = line.replace("no", "0").replace("\n", "")

    container, contents = line[:-1].split(" bags contain ")
    contents = contents.replace(" bags", "").replace(" bag", "")

    # [["name", amount], ["name", amount]]
    contents = [[x[x.index(" ") + 1:], int(x[:x.index(" ")])] for x in contents.split(", ")]

    bags.append([container, contents])

def sub_bags(x):
  total = 1

  for bag, children in bags:
    if bag == x:
      for child, amount in children:
        total += sub_bags(child) * amount

      break

  return total

print(sub_bags("shiny gold"))