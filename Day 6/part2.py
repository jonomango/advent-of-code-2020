import string

sm = 0

with open("input.txt", "r") as file:
  for group in (file.read() + "\n").split("\n\n"):
    curr = 0

    for letter in string.ascii_lowercase:
      invalid = False

      for person in group.split("\n"):
        if letter not in person:
          invalid = True

      if not invalid:
        curr += 1

    sm += curr

print(sm)