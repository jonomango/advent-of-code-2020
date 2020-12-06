import string

sm = 0

with open("input.txt", "r") as file:
  for group in file.read().split("\n\n"):
    curr = 0

    for letter in string.ascii_lowercase:
      if letter in group:
        curr += 1

    sm += curr

print(sm)